from custom_tool import TemplateDocTool
import os

def test_template_doc():
    # Initialize the tool
    template_tool = TemplateDocTool()
    
    # Test template path
    template_path = "D:/c2.0/multi_agent_legal_draft_automation/src/multi_agent_legal_draft_automation/tools/template.docx"
    
    # Test output path
    output_path = "D:/c2.0/multi_agent_legal_draft_automation/src/multi_agent_legal_draft_automation/tools/output_from_template.docx"
    
    # Test replacements
    replacements = {
        "applicant_mark": "HAYSTACK BURGERS & BARLEY",
        "conflicting_mark": "BURGERS & BARLEY",
        "selected_argument_1": "The dissimilarity of the marks in their entireties as to appearance, sound, connotation and commercial impression",
        "draft_1": "The marks differ significantly in appearance and commercial impression. The addition of 'HAYSTACK' creates a distinctive visual and conceptual difference that consumers will immediately notice.",
        "selected_argument_2": "The dissimilarity and nature of the goods or services and trade channels of the two marks",
        "draft_2": "While both establishments offer restaurant services, Applicant's services are more specialized, focusing on a full-service restaurant with a wider menu including craft beer and various beverages.",
        "selected_argument_3": "The conditions under which and buyers to whom sales are made, sophisticated purchasing",
        "draft_3": "The target consumers of Applicant's services are sophisticated diners who pay attention to restaurant names and are unlikely to be confused between the two establishments."
    }
    
    try:
        # Test the tool
        result = template_tool._run(
            template_path=template_path,
            output_path=output_path,
            replacements=replacements,
            placeholder_format="{{placeholder}}"
        )
        
        # Print the results
        print("\n=== Template Processing Result ===")
        print(result)
        print("\n=== Test Completed Successfully ===")
        
        # Verify file was created
        if os.path.exists(output_path):
            print(f"\nFile created successfully at: {output_path}")
        else:
            print("\nWarning: File was not created!")
        
    except Exception as e:
        print(f"\n=== Test Failed ===")
        print(f"Error: {str(e)}")


test_template_doc() 