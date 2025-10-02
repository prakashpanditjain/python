# get api key from environment variable
# Set up the OpenAI client with your API key

from google import genai

from automate_workflow.google_sheet_work import put_content_to_google_sheet

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client()


def get_content_from_gemini(prompt=None):
    response = client.models.generate_content(
        model="gemini-2.5-flash", contents=prompt
    )
    return response.text


if __name__ == '__main__':
    # content = get_content_from_gemini(
    #     "write a tweet, just a tweet, nothing else on trending topic of AI")
    write_into_sheet = put_content_to_google_sheet(
        "write a tweet, just a tweet, nothing else on DSA in python",
        get_content_from_gemini)

    print(write_into_sheet)
