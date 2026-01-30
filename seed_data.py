from database import SessionLocal
from models import Course, Topic
from models import Course, Topic, Motivation


def seed_data():
    db = SessionLocal()

    print("🔥 FORCE RESET DB")

    db.query(Topic).delete()
    db.query(Course).delete()
    db.commit()

    python = Course(course_name="Python")
    java = Course(course_name="Java")
    dsa = Course(course_name="DSA")
    ml = Course(course_name="Machine Learning")
    cpp = Course(course_name="C++")
    web = Course(course_name="Web Development")

    db.add_all([python, java, dsa, ml, cpp, web])
    db.commit()

    python_topics = [
        Topic(course_id=python.id, topic_name="Introduction to Python", youtube_url="https://youtu.be/_uQrJ0TkZlc"),
        Topic(course_id=python.id, topic_name="Variables & Data Types", youtube_url="https://youtu.be/kqtD5dpn9C8"),
        Topic(course_id=python.id, topic_name="Operators", youtube_url="https://youtu.be/v5MR5JnKcZI"),
        Topic(course_id=python.id, topic_name="Control Statements", youtube_url="https://youtu.be/PqFKRqpHrjw"),
        Topic(course_id=python.id, topic_name="Loops", youtube_url="https://youtu.be/6iF8Xb7Z3wQ"),
        Topic(course_id=python.id, topic_name="Functions", youtube_url="https://youtu.be/9Os0o3wzS_I"),
        Topic(course_id=python.id, topic_name="Lists & Tuples", youtube_url="https://youtu.be/W8KRzm-HUcc"),
        Topic(course_id=python.id, topic_name="Dictionaries & Sets", youtube_url="https://youtu.be/daefaLgNkw0"),
        Topic(course_id=python.id, topic_name="OOP Concepts", youtube_url="https://youtu.be/JeznW_7DlB0"),
        Topic(course_id=python.id, topic_name="File Handling", youtube_url="https://youtu.be/Uh2ebFW8OYM"),
    ]

    java_topics = [
        Topic(course_id=java.id, topic_name="Java Introduction", youtube_url="https://youtu.be/grEKMHGYyns"),
        Topic(course_id=java.id, topic_name="Variables & Data Types", youtube_url="https://youtu.be/GoXwIVyNvX0"),
        Topic(course_id=java.id, topic_name="Operators", youtube_url="https://youtu.be/BSVKUk58K6U"),
        Topic(course_id=java.id, topic_name="Control Flow Statements", youtube_url="https://youtu.be/WPvGqX-TXP0"),
        Topic(course_id=java.id, topic_name="Loops", youtube_url="https://youtu.be/6V8pF6JpT"),
        Topic(course_id=java.id, topic_name="OOP Concepts", youtube_url="https://youtu.be/BSVKUk58K6U"),
        Topic(course_id=java.id, topic_name="Inheritance & Polymorphism", youtube_url="https://youtu.be/8cm1x4bC610"),
        Topic(course_id=java.id, topic_name="Interfaces & Abstract Classes", youtube_url="https://youtu.be/9NQ0mZtP6yA"),
        Topic(course_id=java.id, topic_name="Collections Framework", youtube_url="https://youtu.be/VE_AAUxTUC4"),
        Topic(course_id=java.id, topic_name="Exception Handling", youtube_url="https://youtu.be/1XAfapkBQjk"),
    ]

    dsa_topics = [
        Topic(course_id=dsa.id, topic_name="Introduction to DSA", youtube_url="https://youtu.be/0IAPZzGSbME"),
        Topic(course_id=dsa.id, topic_name="Time & Space Complexity", youtube_url="https://youtu.be/mV3wrLBbuuE"),
        Topic(course_id=dsa.id, topic_name="Arrays", youtube_url="https://youtu.be/n60Dn0UsbEk"),
        Topic(course_id=dsa.id, topic_name="Strings", youtube_url="https://youtu.be/8JZsZ1b1a9A"),
        Topic(course_id=dsa.id, topic_name="Patterns", youtube_url="https://youtu.be/tNm_NNSB3_w"),
        Topic(course_id=dsa.id, topic_name="Recursion", youtube_url="https://youtu.be/M2uO2nMT0Bk"),
        Topic(course_id=dsa.id, topic_name="Linked List", youtube_url="https://youtu.be/q8gdBn9RPeI"),
        Topic(course_id=dsa.id, topic_name="Stack & Queue", youtube_url="https://youtu.be/0rH0u6Qz"),
        Topic(course_id=dsa.id, topic_name="Binary Search", youtube_url="https://youtu.be/fnmisPM6cVo"),
        Topic(course_id=dsa.id, topic_name="Sorting Algorithms", youtube_url="https://youtu.be/ZZuD6iUe3Pc"),
    ]

    ml_topics = [
        Topic(course_id=ml.id, topic_name="Introduction to Machine Learning", youtube_url="https://youtu.be/GwIo3gDZCVQ"),
        Topic(course_id=ml.id, topic_name="Types of Machine Learning", youtube_url="https://youtu.be/ukzFI9rgwfU"),
        Topic(course_id=ml.id, topic_name="Data Preprocessing", youtube_url="https://youtu.be/6YnhoCfHk8A"),
        Topic(course_id=ml.id, topic_name="Linear Regression", youtube_url="https://youtu.be/nk2CQITm_eo"),
        Topic(course_id=ml.id, topic_name="Logistic Regression", youtube_url="https://youtu.be/yIYKR4sgzI8"),
        Topic(course_id=ml.id, topic_name="Classification Algorithms", youtube_url="https://youtu.be/5ymGQnJ0Gus"),
        Topic(course_id=ml.id, topic_name="Clustering Algorithms", youtube_url="https://youtu.be/Y5N3F5Iu-6s"),
        Topic(course_id=ml.id, topic_name="Overfitting & Underfitting", youtube_url="https://youtu.be/1dKRdX9bfIo"),
        Topic(course_id=ml.id, topic_name="Model Evaluation", youtube_url="https://youtu.be/85dtiMz9tSo"),
        Topic(course_id=ml.id, topic_name="Introduction to Deep Learning", youtube_url="https://youtu.be/aircAruvnKk"),
    ]

    cpp_topics = [
        Topic(course_id=cpp.id, topic_name="Introduction to C++", youtube_url="https://youtu.be/vLnPwxZdW4Y"),
        Topic(course_id=cpp.id, topic_name="Data Types & Variables", youtube_url="https://youtu.be/ZzaPdXTrSb8"),
        Topic(course_id=cpp.id, topic_name="Operators", youtube_url="https://youtu.be/FyN9Yy0xZ2U"),
        Topic(course_id=cpp.id, topic_name="Control Statements", youtube_url="https://youtu.be/7dPdMtBX1d8"),
        Topic(course_id=cpp.id, topic_name="Loops", youtube_url="https://youtu.be/bL-o2xBENY0"),
        Topic(course_id=cpp.id, topic_name="Functions", youtube_url="https://youtu.be/ykM9H6p5HfE"),
        Topic(course_id=cpp.id, topic_name="Pointers", youtube_url="https://youtu.be/DTxHyVn0ODg"),
        Topic(course_id=cpp.id, topic_name="OOP in C++", youtube_url="https://youtu.be/wN0x9eZLix4"),
        Topic(course_id=cpp.id, topic_name="STL Basics", youtube_url="https://youtu.be/g-1Cn3ccwXY"),
        Topic(course_id=cpp.id, topic_name="File Handling", youtube_url="https://youtu.be/nhpA7ZxkXK0"),
    ]

    web_topics = [
        Topic(course_id=web.id, topic_name="Introduction to Web Development", youtube_url="https://youtu.be/Q33KBiDriJY"),
        Topic(course_id=web.id, topic_name="HTML Basics", youtube_url="https://youtu.be/pQN-pnXPaVg"),
        Topic(course_id=web.id, topic_name="CSS Basics", youtube_url="https://youtu.be/yfoY53QXEnI"),
        Topic(course_id=web.id, topic_name="JavaScript Basics", youtube_url="https://youtu.be/W6NZfCO5SIk"),
        Topic(course_id=web.id, topic_name="DOM Manipulation", youtube_url="https://youtu.be/0ik6X4DJKCc"),
        Topic(course_id=web.id, topic_name="Responsive Design", youtube_url="https://youtu.be/srvUrASNj0s"),
        Topic(course_id=web.id, topic_name="Git & GitHub", youtube_url="https://youtu.be/RGOj5yH7evk"),
        Topic(course_id=web.id, topic_name="REST APIs", youtube_url="https://youtu.be/Q-BpqyOT3a8"),
        Topic(course_id=web.id, topic_name="Frontend vs Backend", youtube_url="https://youtu.be/XBu54nfzxAQ"),
        Topic(course_id=web.id, topic_name="Deploying Web Apps", youtube_url="https://youtu.be/nhBVL41-_Cw"),
    ]

    motivations = [
    Motivation(message="🔥 Great job! Keep going."),
    Motivation(message="💪 Consistency beats talent."),
    Motivation(message="🚀 One step closer to success."),
    Motivation(message="👏 You are doing amazing."),
    Motivation(message="📈 Progress, not perfection."),
    Motivation(message="🏆 Hard work always pays off."),
    Motivation(message="⏳ Every minute you study builds your future."),
    Motivation(message="🧠 Discipline today = freedom tomorrow."),
    Motivation(message="🚶‍♂️ Small steps every day lead to big wins."),
    Motivation(message="🌱 You are growing, even if it feels slow."),
    Motivation(message="⚡ Don’t stop now, you’re on a streak!"),
    Motivation(message="📚 Knowledge compounds like interest."),
    Motivation(message="🔥 Show up daily. Results will follow."),
    Motivation(message="🎯 Focus. Finish. Repeat."),
    Motivation(message="🏃‍♂️ Winners don’t quit, they adapt."),
    Motivation(message="💡 You didn’t come this far to stop."),
    Motivation(message="🛠️ Skills today, success tomorrow."),
    Motivation(message="🚀 Your future self will thank you."),
    Motivation(message="👊 One topic done. Momentum unlocked."),
    Motivation(message="📌 Stay consistent, stay dangerous."),
    Motivation(message="🌟 Excellence is a habit, not an act."),
]


    db.add_all(
        python_topics +
        java_topics +
        dsa_topics +
        ml_topics +
        cpp_topics +
        web_topics+motivations
    )

    db.commit()
    db.close()

    print("✅ ALL COURSES & TOPICS SEEDED SUCCESSFULLY")
