from google import genai

client = genai.Client(api_key="AIzaSyDG-qm7wbNu0nPjaw5KnVbgz6ES0AT6ErI")
response = client.models.generate_content(
    model="gemini-flash-latest",
    contents="someone we were just discussing"
)

print(response.text)