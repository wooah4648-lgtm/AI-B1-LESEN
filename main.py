# -*- coding: utf-8 -*-
from fastapi import FastAPI
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# 加上這段，網頁才准許連線
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class ThemeRequest(BaseModel):
    theme: str

# 🎯 題庫修正：精準補上 correct_answer 索引 (0=A, 1=B, 2=C)
fake_ai_database = {
    "reisen": {
        "text": "Obwohl das Reisen in ferne Länder heutzutage immer günstiger wird, entscheiden sich viele Menschen aus Gründen des Umweltschutzes für den Urlaub im eigenen Land. Eine aktuelle Studie zeigt, dass der CO2-Ausstoß durch den Flugverkehr in den letzten Jahren drastisch gestiegen ist. Wer dennoch fliegt, versucht oft, den Schaden durch finanzielle Beiträge zu Klimaprojekten zu kompensieren. Experten raten dazu, längere Reisen zu planen, anstatt mehrmals im Jahr für wenige Tage zu verreisen, damit sich die CO2-Bilanz verbessert.",
        "question": "Welche Maßnahme wird im Text erwähnt, um die Umweltbelastung beim Fliegen zu verringern?",
        "options": [
            "Man sollte mehrmals im Jahr Kurzreisen mit dem Flugzeug unternehmen.",
            "Man kann finanzielle Beiträge leisten, um den CO2-Ausstoß zu kompensieren.",
            "Man sollte den Urlaub ausschließlich im Ausland verbringen."
        ],
        "correct_answer": 1,
        "explanation": "文中明確提到 'versucht oft, den Schaden durch finanzielle Beiträge zu Klimaprojekten zu kompensieren'（常試圖透過對氣候專案提供經濟貢獻來彌補損害），故選 B。"
    },
    "reise": {
        "text": "Obwohl das Reisen in ferne Länder heutzutage immer günstiger wird, entscheiden sich viele Menschen aus Gründen des Umweltschutzes für den Urlaub im eigenen Land. Eine aktuelle Studie zeigt, dass der CO2-Ausstoß durch den Flugverkehr in den letzten Jahren drastisch gestiegen ist. Wer dennoch fliegt, versucht oft, den Schaden durch finanzielle Beiträge zu Klimaprojekten zu kompensieren. Experten raten dazu, längere Reisen zu planen, anstatt mehrmals im Jahr für wenige Tage zu verreisen, damit sich die CO2-Bilanz verbessert.",
        "question": "Welche Maßnahme wird im Text erwähnt, um die Umweltbelastung beim Fliegen zu verringern?",
        "options": [
            "Man sollte mehrmals im Jahr Kurzreisen mit dem Flugzeug unternehmen.",
            "Man kann finanzielle Beiträge leisten, um den CO2-Ausstoß zu kompensieren.",
            "Man sollte den Urlaub ausschließlich im Ausland verbringen."
        ],
        "correct_answer": 1,
        "explanation": "文中明確提到 'versucht oft, den Schaden durch finanzielle Beiträge zu Klimaprojekten zu kompensieren'，故選 B。"
    },
    "musik": {
        "text": "In unserer modernen Gesellschaft wird Musik nicht mehr nur zur Unterhaltung gehört, sondern auch gezielt in der... Wichtig ist jedoch, dass die Musik keine Liedtexte enthält, da das Gehirn sonst abgelenkt wird.",
        "question": "Warum sollten Studierende laut dem Text Musik ohne Text beim Lernen hören?",
        "options": [
            "Weil Lieder mit Texten zu viel emotionale Unruhe stiften.",
            "Weil das Gehirn durch den sprachlichen Inhalt abgelenkt werden kann.",
            "Weil klassische Musik grundsätzlich immer einen Text haben muss."
        ],
        "correct_answer": 1,
        "explanation": "文章最後一句提到 'da das Gehirn sonst abgelenkt wird'（否則大腦會分心），因為語言內容會分散注意力，故選 B。"
    },
    "umwelt": {
        "text": "Die Reduzierung von Plastikmüll im Alltag stellt eine der größten Herausforderungen unserer Zeit dar... Um diesem Trend entgegenzuwirken, fordern Umweltschützer strengere Gesetze und höhere Steuern auf Plastikprodukte.",
        "question": "Was fordern Umweltschützer, um den Plastikkonsum zu reduzieren?",
        "options": [
            "Die Abschaffung von Stofftaschen in den Supermärkten.",
            "Die Einführung von strengeren Gesetzen und höheren Steuern auf Plastik.",
            "Dass Verbraucher mehr Einwegverpackungen aus Bequemlichkeit kaufen."
        ],
        "correct_answer": 1,
        "explanation": "文中提到 'fordern Umweltschützer strengere Gesetze und höhere Steuern auf Plastikprodukte'（環保人士要求更嚴格的法律和更高的塑料稅），故選 B。"
    },
    "sport": {
        "text": "Regelmäßige körperliche Aktivität gilt als grundlegende Voraussetzung für ein gesundes Leben im Alter... Sportmediziner betonen, dass es nicht auf die Intensität des Trainings ankommt, sondern auf die Regelmäßigkeit.",
        "question": "Was ist laut Sportmedizinern entscheidend für den gesundheitlichen Erfolg des Trainings?",
        "options": [
            "Dass man möglichst schwere Gewichte im Fitnessstudio hebt.",
            "Dass die körperliche Aktivität regelmäßig durchgeführt wird.",
            "Dass ältere Menschen die gleiche Intensität wie jüngere erreichen."
        ],
        "correct_answer": 1,
        "explanation": "體育醫生強調 'dass es nicht auf die Intensität des Trainings ankommt, sondern auf die Regelmäßigkeit'（重要的不是訓練強度，而是規律性），故選 B。"
    },
    "lernen": {
        "text": "Der Erfolg beim Erwerb einer Fremdsprache hängt maßgeblich von der Lernmethode ab... Vielmehr ist es notwendig, die Sprache aktiv anzuwenden, indem man Radio hört, Zeitungsartikel liest und Gespräche sucht.",
        "question": "Welche Aussage entspricht den Informationen im Text?",
        "options": [
            "Ohne einen Auslandsaufenthalt kann man das B1-Niveau niemals erreichen.",
            "Das Auswendiglernen von Grammatik reicht für eine fließende Konversation aus.",
            "Die active Anwendung der Sprache im Alltag ist für den... notwendig."
        ],
        "correct_answer": 2,
        "explanation": "文中指出 'Vielmehr ist es notwendig, die Sprache aktiv anzuwenden'（在日常生活中積極應用語言是必要的），故選 C。"
    },
    "hobby": {
        "text": "In der heutigen Leistungsgesellschaft suchen immer mehr Menschen nach einem sinnvollen Ausgleich... Wichtig ist, dass kein Leistungsdruck entsteht, damit die Freizeitbeschäftigung ihre positive Wirkung entfalten kann.",
        "question": "Was ist laut dem Text wichtig, damit ein Hobby seine positive Wirkung zeigt?",
        "options": [
            "Man muss mit dem Hobby möglichst viel Geld verdienen.",
            "Bei der Freizeitbeschäftigung darf kein Leistungsdruck entstehen.",
            "Man sollte sich auf Aktivitäten beschränken, die körperlich anstrengend sind."
        ],
        "correct_answer": 1,
        "explanation": "文中明確說明 'Wichtig ist, dass kein Leistungsdruck entsteht'（重要的是不能產生表現壓力），故選 B。"
    },
    "essen": {
        "text": "Die Ernährungsgewohnheiten haben sich in den letzten Jahrzehnten stark verändert... Wer selbst kocht, hat nicht nur die Kontrolle über die Zutaten, sondern spart langfristig auch Geld.",
        "question": "Welchen Vorteil hat es laut dem Text, wenn man seine Mahlzeiten selbst zubereitet?",
        "options": [
            "Man verbraucht beim Kochen deutlich weniger Zeit als bei Fertiggerichten.",
            "Man kann dadurch die Kontrolle über die verwendeten Zutaten behalten.",
            "Man ist gezwungen, ausschließlich teure Bio-Produkte zu kaufen."
        ],
        "correct_answer": 1,
        "explanation": "文中提到 'Wer selbst kocht, hat nicht nur die Kontrolle über die Zutaten'（自己煮飯的人不僅能控制食材），故選 B。"
    },
    "arbeit": {
        "text": "Auf dem modernen Arbeitsmarkt wird von Arbeitnehmern immer mehr Flexibilität erwartet... Viele Angestellte neigen dazu, im Homeoffice mehr Überstunden zu machen, da die Grenze zwischen Arbeitszeit und Privatleben verschwimmt.",
        "question": "Welche Risiko wird im Text bezüglich des Arbeitens im Homeoffice genannt?",
        "options": [
            "Dass die Angestellten zu wenig arbeiten und ihre Aufgaben vernachlässigen.",
            "Dass die Grenze zwischen Arbeit und Privatleben verschwimmt und man mehr Überstunden macht.",
            "Dass Unternehmen die flexiblen Arbeitszeiten komplett abschaffen werden."
        ],
        "correct_answer": 1,
        "explanation": "文中指出風險在於 'da die Grenze zwischen Arbeitszeit und Privatleben verschwimmt'（工作與私人生活界線模糊且加班變多），故選 B。"
    }
}

@app.post("/get-quiz")
def get_quiz(data: ThemeRequest):
    theme_key = data.theme.strip().lower()
    if theme_key in fake_ai_database:
        return fake_ai_database[theme_key]
    else:
        return fake_ai_database["hobby"]