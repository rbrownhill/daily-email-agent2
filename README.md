# daily-email-agent2
first attempt at GitHub Agentic workflow using openai key

3/18/2026
1. I went to settings actions general to add workflow permissions
2. I added a Google AI Studio key at settings Secrets_And_Variables Actions
3. I added a temporary variable to use Node.js 24 until it becomes standard in April

4. I told copilot to configure this new repository for github agentic workflow.
I had to manually create a new file .github/workflows/agentic-workflow.yml due to permission issues.

6. I made my own workflow just for email by doing Actions setup_a_workflow_yourself and creating
  .github/workflows/daily-email2.yml
   The only way I can delete an workflow is to delete this file.

8. I created a gmail app password to be able to send the email.

