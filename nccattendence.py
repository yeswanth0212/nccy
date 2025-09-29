# Install Streamlit and pyngrok
!pip install streamlit pyngrok

# Authenticate ngrok
!ngrok authtoken YOUR_NGROK_AUTH_TOKEN
!pip install streamlit pyngrok reportlab

!ngrok authtoken "33NEYBEvzXfsNRgckQgH7vLXdRX_2jvarbZ7sSCnweeLXJyH7"

%%writefile /content/AttendanceSystem.py
import streamlit as st
import datetime
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import datetime
import pytz
# =========================
# III Year Cadets only
# =========================
cadets = [
    ("TN23SDA614001", "CPL", "ABISHEK P"),
    ("TN23SDA614003", "SGT", "HARIKARAN G"),
    ("TN23SDA614005", "CSM", "ROCHAN M"),
    ("TN23SDA614007", "CUO", "SHANJAI VADIVEL S"),
    ("TN23SDA614009", "CPL", "SUDHARSAN N"),
    ("TN23SDA614011", "SGT", "SURHENDHAAR V"),
    ("TN23SDA614012", "CPL", "VISHNU S"),
    ("TN23SDA614013", "CQMS", "YESWANTH S"),
    ("TN23SWA614015", "SGT", "DEVADARSHINI S"),
    ("TN23SWA614016", "CUO", "JEEVIKA V"),
    ("TN23SWA614017", "CPL", "NITHYANANTHINI D A"),
    ("TN23SWA614018", "CPL", "RAJESHWARI E"),
    ("TN23SWA614019", "CPL", "SANDHIYA L"),
    ("TN23SWA614020", "CSM", "SARIHA SRI K"),
     ("TN24SDA614001", "LCPL", "ADITHYA M"),
    ("TN24SDA614002", "LCPL", "ARUNKUMAR S"),
    ("TN24SDA614003", "LCPL", "BENNY PETER JOHNSON C"),
    ("TN24SDA614005", "LCPL", "JAGATHISH S"),
    ("TN24SDA614006", "LCPL", "JAGADEESH V"),
    ("TN24SDA614007", "LCPL", "JANARTHANAN G"),
    ("TN24SDA614009", "LCPL", "KAVIN PRABHAKAR R"),
    ("TN24SDA614010", "LCPL", "NITHISH RAJ A"),
    ("TN24SDA614011", "LCPL", "SANTHOSH KUMAR V"),
    ("TN24SDA614012", "LCPL", "SHARVESH R"),
    ("TN24SWA614014", "LCPL", "DHARANI B"),
    ("TN24SWA614017", "LCPL", "LEGA LAKSHMI A"),
    ("TN24SWA614018", "LCPL", "MADHUMITHRA N"),
    ("TN24SWA614019", "LCPL", "MOHANA PRIYA G"),
    ("TN24SWA614024", "LCPL", "SUBASHREE B"),
]

st.title("📋 NCC Cadets Attendance System")

# Initialize attendance
if "attendance" not in st.session_state:
    st.session_state.attendance = {cadet: False for cadet in cadets}

st.subheader("Mark Attendance")
for cadet in cadets:
    reg_no, rank, name = cadet
    label = f"{reg_no} | {rank} | {name}"
    st.session_state.attendance[cadet] = st.checkbox(label, value=st.session_state.attendance.get(cadet, False))

# Attendance calculation
present = [c for c, status in st.session_state.attendance.items() if status]
absent = [c for c, status in st.session_state.attendance.items() if not status]

st.write(f"✅ **Total Present:** {len(present)}")
st.write(f"❌ **Total Absent:** {len(absent)}")

if absent:
    st.write("🚫 **Absent Cadets:**")
    for cadet in absent:
        st.write(f"- {cadet[0]} | {cadet[1]} | {cadet[2]}")
else:
    st.success("🎉 All cadets are present today!")

# PDF Report Generation
def generate_pdf(filename, date, present, absent, total_present, total_absent):
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter

    c.setFont("Helvetica-Bold", 16)
    c.drawString(200, height - 50, "Attendance Report")

    c.setFont("Helvetica", 12)
    c.drawString(50, height - 100, f"Date: {date}")
    c.drawString(50, height - 120, f"Total Present: {total_present}")
    c.drawString(50, height - 140, f"Total Absent: {total_absent}")

    c.drawString(50, height - 180, "Absent Cadets:")
    y = height - 200
    if not absent:
        c.drawString(70, y, "None (All Present)")
    else:
        for cadet in absent:
            text = f"{cadet[0]} | {cadet[1]} | {cadet[2]}"
            c.drawString(70, y, text)
            y -= 20

    c.save()

if st.button("📥 Download Attendance Report as PDF"):
    india_tz = pytz.timezone("Asia/Kolkata")
    now = datetime.datetime.now(india_tz).strftime("%Y-%m-%d %H:%M:%S")
    filename = "attendance_report.pdf"
    generate_pdf(filename, now, present, absent, len(present), len(absent))

    with open(filename, "rb") as f:
        st.download_button(
            label="📄 Download PDF",
            data=f,
            file_name=filename,
            mime="application/pdf"
        )


from pyngrok import ngrok
import subprocess

# Kill old tunnels if running
ngrok.kill()

# Start new tunnel
public_url = ngrok.connect(8501)
print("🚀 Public URL:", public_url)

# Launch Streamlit app
subprocess.Popen(["streamlit", "run", "/content/AttendanceSystem.py"])

