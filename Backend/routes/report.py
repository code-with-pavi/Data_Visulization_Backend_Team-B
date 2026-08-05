from flask import Blueprint, send_file
from services.report_service import generate_pdf_report

report_bp = Blueprint("report", __name__)


@report_bp.route("/pdf", methods=["GET"])
def download_pdf():

    pdf_path = generate_pdf_report()

    return send_file(
        pdf_path,
        as_attachment=True,
        download_name="Threat_Report.pdf",
        mimetype="application/pdf"
    )