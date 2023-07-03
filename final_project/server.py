from flask import Flask, render_template, request

from machinetranslation import translator

app = Flask("Web Translator")


@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    translated = translator.englishToFrench(textToTranslate)
    return f"Translated text to French: {translated}"


@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    translated = translator.frenchToEnglish(textToTranslate)
    return f"Translated text to English: {translated}"


@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
