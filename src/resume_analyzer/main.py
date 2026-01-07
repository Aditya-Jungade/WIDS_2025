#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from resume_analyzer.crew import ResumeAnalyzer

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

TARGET_JOB_DESCRIPTION = """
Senior Software Engineer (Python/Cloud)
Requirements:
- 5+ years experience with Python and Django/FastAPI
- Experience with AWS (Lambda, EC2, S3)
- Strong understanding of REST APIs and Microservices
- Leadership experience mentoring junior devs
- "Go-getter" attitude and strong communication skills.
"""

CANDIDATE_RESUME = """
John Doe
Software Developer
Experience:
- Built web apps using Python and Flask.
- Managed database migrations.
- Worked with Docker and Kubernetes.
"""

def run():
    """
    Run the crew.
    """
    inputs = {
        'resume': CANDIDATE_RESUME,
        'job_description': TARGET_JOB_DESCRIPTION
    }

    try:
        ResumeAnalyzer().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        'resume': CANDIDATE_RESUME,
        'job_description': TARGET_JOB_DESCRIPTION
    }
    try:
        ResumeAnalyzer().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        ResumeAnalyzer().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        'resume': CANDIDATE_RESUME,
        'job_description': TARGET_JOB_DESCRIPTION
    }

    try:
        ResumeAnalyzer().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

# def run_with_trigger():
#     """
#     Run the crew with trigger payload.
#     """
#     import json

#     if len(sys.argv) < 2:
#         raise Exception("No trigger payload provided. Please provide JSON payload as argument.")

#     try:
#         trigger_payload = json.loads(sys.argv[1])
#     except json.JSONDecodeError:
#         raise Exception("Invalid JSON payload provided as argument")

#     inputs = {
#         "crewai_trigger_payload": trigger_payload,
#         "topic": "",
#         "current_year": ""
#     }

#     try:
#         result = ResumeAnalyzer().crew().kickoff(inputs=inputs)
#         return result
#     except Exception as e:
#         raise Exception(f"An error occurred while running the crew with trigger: {e}")
