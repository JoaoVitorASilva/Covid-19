import http.client, urllib.parse, json, time

host = "vso-rg-0312326.cognitiveservices.azure.com"
service = "/qnamaker/v4.0"
method = "/knowledgebases/create"

path = service + method

kb_model = {
    "name": "QnA Maker FAQ",
    "qbaList": [
        {
            "id": 0,
            "answer": "Resposta.",
            "source": "Custom Editorial",
            "questions": [
                "Pergunta",
                "Pergunta?"
            ],
            "metadata": [
                {
                    "name": "category",
                    "value": "api"
                }
            ]
        }
    ],
    "urls": [],
    "files": []
}