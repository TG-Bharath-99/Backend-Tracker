from database import SessionLocal
from models import Course, Topic

db = SessionLocal()

# ---------------- COURSES ----------------
courses = [
    Course(course_name="Python"),
    Course(course_name="Java"),
    Course(course_name="DSA"),
    Course(course_name="Machine Learning"),
]

db.add_all(courses)
db.commit()

# ---------------- FETCH COURSES ----------------
python = db.query(Course).filter_by(course_name="Python").first()
java = db.query(Course).filter_by(course_name="Java").first()
dsa = db.query(Course).filter_by(course_name="DSA").first()
ml = db.query(Course).filter_by(course_name="Machine Learning").first()

# ---------------- PYTHON TOPICS ----------------
python_topics = [
    Topic(course_id=python.id, topic_name="Basics", youtube_url="https://youtu.be/_uQrJ0TkZlc"),
    Topic(course_id=python.id, topic_name="Variables", youtube_url="https://youtu.be/kqtD5dpn9C8"),
    Topic(course_id=python.id, topic_name="Loops", youtube_url="https://youtu.be/6iF8Xb7Z3wQ"),
    Topic(course_id=python.id, topic_name="Functions", youtube_url="https://youtu.be/9Os0o3wzS_I"),
]

# ---------------- JAVA TOPICS ----------------
java_topics = [
    Topic(course_id=java.id, topic_name="Basics", youtube_url="https://youtu.be/grEKMHGYyns"),
    Topic(course_id=java.id, topic_name="OOPS", youtube_url="https://youtu.be/BSVKUk58K6U"),
    Topic(course_id=java.id, topic_name="Collections", youtube_url="https://youtu.be/rZxZcLxa3X0"),
]

# ---------------- DSA TOPICS ----------------
dsa_topics = [
    Topic(course_id=dsa.id, topic_name="Arrays", youtube_url="https://youtu.be/n60Dn0UsbEk"),
    Topic(course_id=dsa.id, topic_name="Linked List", youtube_url="https://youtu.be/qp8u-frRAnU"),
    Topic(course_id=dsa.id, topic_name="Stack & Queue", youtube_url="https://youtu.be/1n0Q9xj5p6I"),
    Topic(course_id=dsa.id, topic_name="Recursion", youtube_url="https://youtu.be/M2uO2nMT0Bk"),
]

# ---------------- ML TOPICS ----------------
ml_topics = [
    Topic(course_id=ml.id, topic_name="Introduction to ML", youtube_url="https://youtu.be/GwIo3gDZCVQ"),
    Topic(course_id=ml.id, topic_name="Linear Regression", youtube_url="https://youtu.be/nk2CQITm_eo"),
    Topic(course_id=ml.id, topic_name="Classification", youtube_url="https://youtu.be/7eh4d6sabA0"),
]

# ---------------- INSERT ALL ----------------
db.add_all(
    python_topics +
    java_topics +
    dsa_topics +
    ml_topics
)

db.commit()
db.close()

print("✅ All courses & topics inserted successfully")
