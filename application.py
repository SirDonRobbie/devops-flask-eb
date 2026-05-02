from flask import Flask, jsonify, render_template_string, request
import logging

application = Flask(__name__)

logging.basicConfig(level=logging.INFO)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>DevOps Flask App</title>
</head>
<body>
    <h1>DevOps Flask App on AWS Elastic Beanstalk</h1>
    <p>This app demonstrates CI/CD, Infrastructure as Code, cloud deployment,
    testing, security awareness and observability.</p>

    <form action="/message" method="get">
        <label>Enter your name:</label>
        <input name="name" placeholder="Your name">
        <button type="submit">Submit</button>
    </form>

    <p><a href="/health">Health Check</a></p>
</body>
</html>
"""


@application.route("/")
def home():
    application.logger.info("Home page requested")
    return render_template_string(HTML)


@application.route("/message")
def message():
    name = request.args.get("name", "DevOps learner")
    application.logger.info("Message page requested for name=%s", name)
    return (
        f"Hello, {name}. "
        "Your Flask app has been deployed through a DevOps pipeline!"
    )


@application.route("/health")
def health():
    application.logger.info("Health check requested")
    return jsonify(status="healthy", service="devops-flask-eb"), 200


if __name__ == "__main__":
    application.run(host="0.0.0.0", port=5000)


