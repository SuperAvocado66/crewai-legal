"""
Test script to verify that the updated TemplateDocTool correctly handles the existing template.
"""

from custom_tool import TemplateDocTool
import os

def test_existing_template():
    """Test that the TemplateDocTool correctly processes the existing template."""
    # Path to the existing template
    template_path = "D:/c2.0/multi_agent_legal_draft_automation/src/multi_agent_legal_draft_automation/tools/template.docx"
    
    # Create the output path
    output_path = "D:/c2.0/multi_agent_legal_draft_automation/src/multi_agent_legal_draft_automation/tools/existing_template_output.docx"
    
    # Create the replacements
    replacements = {
        "applicant_mark": "HAYSTACK BURGERS & BARLEY",
        "conflicting_mark": "BURGERS & BARLEY",
        "applicant_mark_goods_and_services": "Restaurant services, specifically a full-service restaurant offering burgers, sandwiches, salads, craft beer, and various beverages.",
        "conflicting_mark_goods_and_services": "Restaurants, restaurant and bar services including carryout services.",
        "selected_argument_1": "The dissimilarity of the marks in their entireties as to appearance, sound, connotation and commercial impression",
        "selected_argument_2": "The dissimilarity of goods and services and trade channels of the two marks",
        "selected_argument_3": "The conditions under which and buyers to whom sales are made, sophisticated purchasing",
        "draft_1": "The marks differ significantly in appearance and commercial impression. The addition of 'HAYSTACK' creates a distinctive visual and conceptual difference that consumers will immediately notice.",
        "draft_2": "While both establishments offer restaurant services, Applicant's services are more specialized, focusing on a full-service restaurant with a wider menu including craft beer and various beverages.",
        "draft_3": "The target consumers of Applicant's services are sophisticated diners who pay attention to restaurant names and are unlikely to be confused between the two establishments."
    }
    
    # Initialize the tool
    tool = TemplateDocTool()
    
    # Process the template
    result = tool._run(
        template_path=template_path,
        output_path=output_path,
        replacements=replacements
    )
    
    print(result)
    
    if os.path.exists(output_path):
        print(f"Output file created at {output_path}")
        print("Please open the file to verify that placeholders were correctly replaced.")
    else:
        print("Output file was not created.")

if __name__ == "__main__":
    test_existing_template() 