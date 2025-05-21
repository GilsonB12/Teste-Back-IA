from flask import Blueprint, request, jsonify
from uuid import UUID
from werkzeug.exceptions import RequestEntityTooLarge
from flasgger import swag_from
from ..services.ocr_service import extract_text
from ..services.summarizer_service import summarize
from ..services.llm_service import generate_decision
from ..models.log_model import log_request

process_bp = Blueprint("process", __name__)

@process_bp.app_errorhandler(RequestEntityTooLarge)
def handle_413(e):
    return jsonify({"error": "Upload muito grande maximo permitido: 100MB."}), 413


@process_bp.route("/process", methods=["POST"])
@swag_from({
    'tags': ['Processamento'],
    'summary': 'Processa currículos com OCR e LLM',
    'description': 'Recebe múltiplos arquivos (PDF/PNG/JPEG), realiza OCR e gera sumário. Se uma query for enviada, responde com decisão baseada nos resumos.',
    'consumes': ['multipart/form-data'],
    'parameters': [
        {
            'name': 'files',
            'in': 'formData',
            'type': 'array',
            'items': {'type': 'file', 'format': 'binary'},
            'required': True,
            'description': 'Arquivos PDF, PNG ou JPEG (multi-upload)',
            'collectionFormat': 'multi'
        },
        {
            'name': 'request_id',
            'in': 'formData',
            'type': 'string',
            'required': True,
            'description': 'UUID da requisição (ex: 123e4567-e89b-12d3-a456-426614174000)'
        },
        {
            'name': 'user_id',
            'in': 'formData',
            'type': 'string',
            'required': True,
            'description': 'ID do usuário (ex: usuario_teste)'
        },
        {
            'name': 'query',
            'in': 'formData',
            'type': 'string',
            'required': False,
            'description': 'Query opcional, ex: "Qual currículo é mais adequado para vaga de Engenheiro de Software?"'
        }
    ],
    'responses': {
        200: {
            'description': 'Processamento concluído com sucesso.',
            'examples': {
                'application/json': {
                    'Sem query': {
                        "summaries": {
                            "cv1.pdf": "Resumo automático do currículo...",
                            "cv2.png": "Resumo automático do currículo..."
                        }
                    },
                    'Com query': {
                        "summaries": {
                            "cv1.pdf": "Resumo automático...",
                            "cv2.png": "Resumo automático..."
                        },
                        "decision": "O currículo cv1.pdf é o mais adequado, pois menciona Python, IA e MongoDB."
                    }
                }
            }
        },
        400: {
            'description': 'Erro na requisição',
            'examples': {
                'application/json': {
                    'error': 'request_id inválido'
                }
            }
        },
        413: {
            'description': 'Payload muito grande',
            'examples': {
                'application/json': {
                    'error': 'Upload muito grande. Máximo permitido: 100MB.'
                }
            }
        },
        500: {
            'description': 'Erro interno inesperado',
            'examples': {
                'application/json': {
                    'error': 'Erro durante o processamento'
                }
            }
        }
    }
})
def process():
    try:
        files = request.files.getlist("files")
        if not files:
            return jsonify({"error": "Nenhum arquivo enviado"}), 400

        request_id = request.form.get("request_id")
        user_id = request.form.get("user_id")
        query = request.form.get("query", None)

        try:
            UUID(request_id)
        except:
            return jsonify({"error": "request_id invalido"}), 400
        if not user_id:
            return jsonify({"error": "user_id é obrigatorio"}), 400

        extracted = {f.filename: extract_text(f) for f in files}
        summaries = {fname: summarize(text) for fname, text in extracted.items()}

        result = {"summaries": summaries}
        if query:
            result["decision"] = generate_decision(summaries, query)

        log_request(request_id, user_id, query, result)
        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500
