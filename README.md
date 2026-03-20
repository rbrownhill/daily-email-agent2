# daily-email-agent2
first attempt at GitHub Agentic workflow using openai key

3/18/2026
1. I went to settings actions general to add workflow permissions
2. I added a Google AI Studio GEMINI_API_KEY at settings Secrets_And_Variables Actions
3. I added a temporary variable to use Node.js 24 until it becomes standard in April

4a. I told copilot to configure this new repository for github agentic workflow.
I had to manually create a new file .github/workflows/agentic-workflow.yml due to permission issues.
The results were confusing, so

4b. I made my own workflow just for email by doing Actions setup_a_workflow_yourself and creating
  .github/workflows/daily-email2.yml
  NOTE: The command workflow_dispatch in the yml file allows me to run the action manually for testing.
     instead of having the cron command do it.
   The only way I can delete an workflow is to delete this file.

5. I created a gmail app password to be able to send the email following examples.
6. I used ai examples to create the api calls to yahoo finance
7. I followed instructions at https://ai.google.dev/gemini-api/docs/quickstart#what's-next
   for the api calls to Gemini AI. There is much more I can learn about possible inputs and outputs.

