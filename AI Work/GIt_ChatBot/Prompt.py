class PromptsStand:
    def __init__(self, message=None):
        self.message = message  # Use 'self.message' to store the input message

    def create_prompts(self, doc, custom=None):
        if custom=='Summary Agent':
            doc=str(doc)
            guidelines ="you should abide by below rules while answering the question=" + str(self.message) + "use this following document as reference " + doc + " Summarize the Answer- Provide a concise, focused summary of the users query or problem. Rate Code Quality-Evaluate clarity, structure, efficiency, and adherence to coding best practices.Analyze Repo Documentation-Check if setup and usage instructions are clear, complete, and easy to follow.Evaluate Understanding Level-Determine the skill level (beginner, intermediate, advanced) required to use the code or repo effectively.Identify Missing Information-Point out any missing documents, examples, or references necessary for full comprehension."
            return guidelines  # If a custom prompt is provided, return it
        else:
              guidelines =print(f"you are a {custom} , please just answer this {self.message} , Also Summarize the Answer:Provide a concise, focused summary of the users query or problem. Rate Code Quality- Evaluate clarity, structure, efficiency, and adherence to coding best practices.Analyze Repo Documentation-Check if setup and usage instructions are clear, complete, and easy to follow.Evaluate Understanding Level-Determine the skill level (beginner, intermediate, advanced) required to use the code or repo effectively.Identify Missing Information-Point out any missing documents, examples, or references necessary for full comprehension.")
        return guidelines  # Otherwise, return the default message

# def main():
#     # Create an instance of PromptsStand with a default message
#     prompt_stand = PromptsStand("This is a default message.")

#     # Test the CreatePrompts method without custom input
#     print(prompt_stand.create_prompts())  # Output: This is a default message.

#     # Test the CreatePrompts method with custom input
#     print(prompt_stand.create_prompts("This is a custom message."))  # Output: This is a custom message.

# if __name__ == "__main__":
#     main()
