#!/usr/bin/env python
import sys
from crew import draft_crew
from tools.model import Placeholder
from dotenv import load_dotenv

load_dotenv()

# This main file is intended to be a way for your to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        'input_list': [
            "The dissimilarity of the marks in their entireties as to appearance, sound, connotation and commercial impression",
            "The dissimilarity and nature of the goods or services and trade channels of the two marks",
            "The conditions under which and buyers to whom sales are made, sophisticated purchasing"
        ],
        'applicant_mark': "HAYSTACK BURGERS & BARLEY",
        'applicant_mark_goods_and_services': "restaurant services, specifically a full-service restaurant offering burgers, sandwiches, salads, chili, appetizers, shakes, desserts, craft beer, and various beverages. The establishment provides both sit-down dining and take-out services, with food and beverages available for consumption both on and off the premises.",
        'conflicting_mark': "BURGERS & BARLEY",
        'conflicting_mark_goods_and_services': "restaurants, restaurant and bar services including carryout services, and take-out restaurant services. The establishment provides both restaurant and bar services with dine-in and carryout options.",
        'template_path': "D:/c2.0/multi_agent_legal_draft_automation/src/multi_agent_legal_draft_automation/tools/template.docx",
    }
    draft_crew().crew().kickoff(inputs=inputs)

run()