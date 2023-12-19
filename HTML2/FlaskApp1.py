from flask import Flask, render_template, request, url_for, flash, redirect

# ...
from FileCsv2 import FileCsv

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ba0b8ea83b16b45383019307faf81ec0cacdc91741b86416'

messages = []

@app.route('/', methods=('GET', 'POST'))
def index():
    colours = ['US', 'CA', 'GB', 'AU', 'DE']

    if request.method == 'POST':
        print(request.form['colour'])
        colour = request.form['colour']

        if not colour:
            print("colour required")
            flash('colour is required!')
        else:
            messages.clear()

            messages.append(
                {'title': "WYNIKI DLA KRAJU ", 'content': [colour]})

            file = FileCsv("C:\\Users\\bkolodzi\\OneDrive - Intel Corporation\\Desktop\\collars\\FutureCollars-main\\FutureCollars-main\\HTML\\ds_salaries.csv")

            content = [file.srednie_zarobki(colour)]
            messages.append({'title': "1.Podaj srednie zarobki dla danego Kraju. Wybierz odpowiedni skrót", 'content': content})

            content = []
            for item in file.najwieksze_place(colour):
                content.append("job_title: " + item[3] + " salary_in_usd: " + str(item[6]) + " USD \n")

            messages.append({'title': "3 firm, które płacą najwięcej w danym kraju", 'content': content})

            licznik = 1
            content = []
            sredniepowyzej = file.procent_powyzej(colour)
            for item in sredniepowyzej:
                content.append("dla firmy " + str(licznik) + " średnia powyżej wynosi: " + str(item) + " % \n")
                licznik += 1
            messages.append({'title': "średnie powyżej 3 firmy, które płacą najwięcej w danym kraju", 'content': content})


            dane = file.rekomendacja(colour)
            content = []
            for item in dane:
                content.append(item)

            messages.append({'title': "Rekomendacja jakie stanowisko Data Science w której firmie jest najbardziej opłacalne w danym kraju. W zależności o doświadczenia są to najlepsze oferty",
                             'content': content})

    return render_template('index.html', messages=messages , colours=colours)
