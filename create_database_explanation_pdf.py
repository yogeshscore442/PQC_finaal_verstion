from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    Flowable,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "Database_Explanation_Tamil.pdf"
FONT_PATH = Path(r"C:\Windows\Fonts\Nirmala.ttc")

if FONT_PATH.exists():
    pdfmetrics.registerFont(TTFont("ProjectFont", str(FONT_PATH), subfontIndex=0))
    FONT = "ProjectFont"
else:
    FONT = "Helvetica"

NAVY = colors.HexColor("#10253F")
BLUE = colors.HexColor("#1D6FA5")
TEAL = colors.HexColor("#0F8B8D")
LIGHT_BLUE = colors.HexColor("#EAF4FA")
LIGHT_TEAL = colors.HexColor("#E8F6F4")
TEXT = colors.HexColor("#1D2939")
MUTED = colors.HexColor("#52606D")
WHITE = colors.white

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(
    name="TitleProject", fontName=FONT, fontSize=26, leading=32,
    textColor=WHITE, alignment=TA_CENTER, spaceAfter=8,
))
styles.add(ParagraphStyle(
    name="SubtitleProject", fontName=FONT, fontSize=13, leading=19,
    textColor=colors.HexColor("#D9F0F2"), alignment=TA_CENTER,
))
styles.add(ParagraphStyle(
    name="HeadingProject", fontName=FONT, fontSize=18, leading=23,
    textColor=NAVY, spaceBefore=4, spaceAfter=9,
))
styles.add(ParagraphStyle(
    name="BodyProject", fontName=FONT, fontSize=10.5, leading=16,
    textColor=TEXT, spaceAfter=6,
))
styles.add(ParagraphStyle(
    name="SmallProject", fontName=FONT, fontSize=8.5, leading=12,
    textColor=MUTED,
))
styles.add(ParagraphStyle(
    name="CardTitle", fontName=FONT, fontSize=11.5, leading=15,
    textColor=BLUE, spaceAfter=4,
))
styles.add(ParagraphStyle(
    name="CardBody", fontName=FONT, fontSize=9.5, leading=14,
    textColor=TEXT,
))
styles.add(ParagraphStyle(
    name="TableHead", fontName=FONT, fontSize=9.5, leading=13,
    textColor=WHITE, alignment=TA_LEFT,
))
styles.add(ParagraphStyle(
    name="TableCell", fontName=FONT, fontSize=8.8, leading=13,
    textColor=TEXT,
))


class Banner(Flowable):
    def __init__(self, title, subtitle):
        super().__init__()
        self.title = title
        self.subtitle = subtitle
        self.width = 170 * mm
        self.height = 55 * mm

    def draw(self):
        canvas = self.canv
        canvas.setFillColor(NAVY)
        canvas.roundRect(0, 0, self.width, self.height, 5 * mm, fill=1, stroke=0)
        canvas.setFillColor(TEAL)
        canvas.rect(0, self.height - 4 * mm, self.width, 4 * mm, fill=1, stroke=0)
        title = Paragraph(self.title, styles["TitleProject"])
        title.wrapOn(canvas, self.width - 20 * mm, 28 * mm)
        title.drawOn(canvas, 10 * mm, 25 * mm)
        subtitle = Paragraph(self.subtitle, styles["SubtitleProject"])
        subtitle.wrapOn(canvas, self.width - 20 * mm, 18 * mm)
        subtitle.drawOn(canvas, 10 * mm, 9 * mm)


def p(text, style="BodyProject"):
    return Paragraph(text, styles[style])


def card(title, body, background=LIGHT_BLUE):
    table = Table([[p(title, "CardTitle")], [p(body, "CardBody")]], colWidths=[81 * mm])
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), background),
        ("BOX", (0, 0), (-1, -1), 0.6, colors.HexColor("#B8D4E5")),
        ("LEFTPADDING", (0, 0), (-1, -1), 5 * mm),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5 * mm),
        ("TOPPADDING", (0, 0), (-1, -1), 3 * mm),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3 * mm),
    ]))
    return table


def bullet(text):
    return p("&#8226; " + text)


def footer(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(colors.HexColor("#D9E2EC"))
    canvas.line(18 * mm, 14 * mm, 192 * mm, 14 * mm)
    canvas.setFont(FONT, 8)
    canvas.setFillColor(MUTED)
    canvas.drawString(18 * mm, 8 * mm, "PQC Secure Communication - Database Explanation")
    canvas.drawRightString(192 * mm, 8 * mm, f"Page {doc.page}")
    canvas.restoreState()


story = []
story.append(Banner(
    "Which Database Does This Project Use?",
    "PQC Secure Communication - Simple Explanation | Database: SQLite",
))
story.append(Spacer(1, 8 * mm))
story.append(p(
    "<b>Short answer:</b> This project uses <b>SQLite</b> as its default database. "
    "The Python application uses <b>Flask-SQLAlchemy</b> to work with the database.",
))
story.append(p(
    "SQLite is a relational database that stores data in a local file and does not require a separate database server. "
    "This makes the project easy to install and run.",
))
story.append(Spacer(1, 3 * mm))
story.append(Table([
    [card("Database type", "SQLite - file-based relational database", LIGHT_TEAL),
     card("Database file", "pqc_chat.db", LIGHT_BLUE)],
    [card("Python connection", "Flask-SQLAlchemy ORM", LIGHT_BLUE),
    card("Default location", "The application's instance folder", LIGHT_TEAL)],
], colWidths=[85 * mm, 85 * mm], style=TableStyle([
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("LEFTPADDING", (0, 0), (-1, -1), 0),
    ("RIGHTPADDING", (0, 0), (-1, -1), 4 * mm),
    ("TOPPADDING", (0, 0), (-1, -1), 2 * mm),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 2 * mm),
])))
story.append(Spacer(1, 5 * mm))
story.append(p("<b>Simple example:</b> Think of SQLite as a digital notebook. The application records users, messages, emails and other information in separate tables."))

story.append(PageBreak())
story.append(p("What Does the Database Do in This Project?", "HeadingProject"))
story.append(p("When the application starts, `db.create_all()` creates the required tables. Information from registration, chat, email and file upload activities is stored in these tables."))
story.append(Table([
    [p("Table", "TableHead"), p("Purpose", "TableHead"), p("Main information stored", "TableHead")],
    [p("users", "TableCell"), p("User account and identity", "TableCell"), p("username, email, password hash, cryptographic keys", "TableCell")],
    [p("messages", "TableCell"), p("Chat messages", "TableCell"), p("encrypted message, IV, authentication tag, signature", "TableCell")],
    [p("emails", "TableCell"), p("Secure email", "TableCell"), p("subject, encrypted body, sender/receiver, signature", "TableCell")],
    [p("attachments", "TableCell"), p("Email/chat files", "TableCell"), p("filename, file size, encrypted file key, SHA3 digest", "TableCell")],
    [p("group_chats", "TableCell"), p("Group chat", "TableCell"), p("group name, admin, creation time", "TableCell")],
    [p("group_members", "TableCell"), p("Group membership", "TableCell"), p("Which users belong to which groups", "TableCell")],
    [p("audit_logs", "TableCell"), p("Security activity tracking", "TableCell"), p("action, algorithm, result, risk level, IP, time", "TableCell")],
    [p("benchmark_results", "TableCell"), p("Performance measurement", "TableCell"), p("Operation time and data size", "TableCell")],
    [p("user_session_keys", "TableCell"), p("Chat session status", "TableCell"), p("session hash, mode, ACTIVE/REVOKED status", "TableCell")],
    [p("user_chat_preferences", "TableCell"), p("Chat settings", "TableCell"), p("Pinned, archived, blocked and locked settings", "TableCell")],
], colWidths=[36 * mm, 53 * mm, 81 * mm], repeatRows=1, style=TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), NAVY),
    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, LIGHT_BLUE]),
    ("GRID", (0, 0), (-1, -1), 0.35, colors.HexColor("#B8C7D5")),
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("LEFTPADDING", (0, 0), (-1, -1), 3 * mm),
    ("RIGHTPADDING", (0, 0), (-1, -1), 3 * mm),
    ("TOPPADDING", (0, 0), (-1, -1), 2.2 * mm),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 2.2 * mm),
])))

story.append(PageBreak())
story.append(p("How Is the Data Protected?", "HeadingProject"))
story.append(p("The key design point is that chat messages and email bodies are not stored as plain text. The database stores the ciphertext created after encryption."))
for item in [
    "Password: The original password is not stored; only the password hash is stored.",
    "Chat message: encrypted_payload, IV, authentication tag and digital signature are stored.",
    "Email: encrypted_body, sender/receiver details and signature information are stored.",
    "File: The encrypted file is kept in server storage; the database keeps file metadata, wrapped key and SHA3 digest.",
    "Audit log: Login events, security actions, success/failure and risk level history are stored.",
]:
    story.append(bullet(item))
story.append(Spacer(1, 5 * mm))
story.append(Table([
    [p("User action", "TableHead"), p("Application", "TableHead"), p("Database", "TableHead")],
    [p("User sends a message", "TableCell"), p("Encrypts and signs it", "TableCell"), p("Stores only ciphertext", "TableCell")],
    [p("Receiver opens the message", "TableCell"), p("Verifies and decrypts it", "TableCell"), p("Reads the stored encrypted data", "TableCell")],
], colWidths=[56 * mm, 56 * mm, 58 * mm], style=TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), TEAL),
    ("BACKGROUND", (0, 1), (-1, -1), LIGHT_TEAL),
    ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#9BCBC7")),
    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ("LEFTPADDING", (0, 0), (-1, -1), 4 * mm),
    ("RIGHTPADDING", (0, 0), (-1, -1), 4 * mm),
    ("TOPPADDING", (0, 0), (-1, -1), 4 * mm),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 4 * mm),
])))
story.append(Spacer(1, 6 * mm))
story.append(p("Important Note", "CardTitle"))
story.append(p("The database stores encrypted data. However, this current prototype stores private keys in database fields. Before production deployment, add encryption at rest, strong secret management and proper access control.", "CardBody"))

story.append(PageBreak())
story.append(p("Can the Database Setting Be Changed?", "HeadingProject"))
story.append(p("Yes. This setting is defined in `app/config.py`:") )
story.append(Table([[p("SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///pqc_chat.db')", "CardBody")]], colWidths=[170 * mm], style=TableStyle([
    ("BACKGROUND", (0, 0), (-1, -1), NAVY),
    ("TEXTCOLOR", (0, 0), (-1, -1), WHITE),
    ("BOX", (0, 0), (-1, -1), 0, NAVY),
    ("LEFTPADDING", (0, 0), (-1, -1), 5 * mm),
    ("RIGHTPADDING", (0, 0), (-1, -1), 5 * mm),
    ("TOPPADDING", (0, 0), (-1, -1), 4 * mm),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 4 * mm),
])))
story.append(Spacer(1, 5 * mm))
story.append(p("What this means:", "CardTitle"))
story.append(bullet("If the `DATABASE_URL` environment variable is not provided, SQLite is used."))
story.append(bullet("If `DATABASE_URL` is provided, SQLAlchemy uses that database connection."))
story.append(bullet("Tests use `sqlite:///:memory:` separately. This is a temporary test database, not the main application database."))
story.append(Spacer(1, 5 * mm))
story.append(p("Final answer", "HeadingProject"))
story.append(p("This project's default database is <b>SQLite</b>, accessed from Python through <b>Flask-SQLAlchemy</b>. User accounts, encrypted chat, secure email, file information, groups and security audit records are stored in relational tables. Important message and email content is stored in encrypted form rather than plain text."))
story.append(Spacer(1, 8 * mm))
story.append(p("Source files: app/config.py, app/models.py, app/__init__.py", "SmallProject"))

doc = SimpleDocTemplate(
    str(OUTPUT), pagesize=A4, rightMargin=20 * mm, leftMargin=20 * mm,
    topMargin=17 * mm, bottomMargin=19 * mm, title="Database Explanation - PQC Secure Communication",
    author="PQC Secure Communication Project",
)
doc.build(story, onFirstPage=footer, onLaterPages=footer)
print(OUTPUT)