from flask import Flask, render_template

app = Flask(__name__)

cards={'starter':['Il Pacchetto Starter è ideale per le piccole imprese, liberi professionisti e startup che desiderano avviare la loro presenza online con un sito web essenziale e professionale. Questo pacchetto offre tutto il necessario per una visibilità iniziale di alta qualità a un prezzo conveniente.',['Sito Web (2 Pagine)','Servizio di Hosting'], 'Mani.jpg'],
       'pro':['Il Pacchetto Pro è la soluzione ideale per le aziende e i professionisti che necessitano di un sito web più ampio e funzionale, con 4 pagine, completo di servizi di hosting e manutenzione. Questo pacchetto è progettato per offrire una gestione senza preoccupazioni e una presenza online professionale.', ['Sito Web (4 Pagine)','Servizio di Hosting','Servizio di Manutenzione'], 'Mani2.jpg'],
       'elite':["Il Pacchetto Elite è la soluzione definitiva per aziende e professionisti che desiderano un sito web di alta qualità, completo di tutte le funzionalità necessarie per una presenza online robusta e coerente con il proprio brand. Con questo pacchetto, ottieni non solo un sito web ben progettato e gestito, ma anche un logo personalizzato", ['Sito Web (4 Pagine)','Servizio di Hosting','Servizio di Manutenzione', 'Logo Personalizzato'], 'Mani3.jpg'],
       'grafico':["Il Pacchetto Graphic è ideale per chi cerca una soluzione efficace per il branding e l’arricchimento visivo del proprio sito o materiale promozionale. Con questo pacchetto, ottieni tre varianti di logo personalizzati e una selezione di immagini stock per arricchire i tuoi contenuti visivi, tutto a un prezzo conveniente.", ['Logo Personalizzato', 'Immagini Stock'], 'Mano4.jpg'],
       'lingue':["Il Pacchetto Language è progettato per aiutarti a raggiungere un pubblico globale, offrendo una traduzione professionale del tuo sito web in tre lingue. Questo pacchetto è ideale per le aziende e i professionisti che desiderano espandere la loro portata e migliorare l'accessibilità del loro sito a utenti di diverse lingue e culture.", ['Traduzione in 3 lingue'], 'Libro.jpg']}

@app.route('/dismissed')
def homeDismissed():
    return render_template('dismissed.html')

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/card/<card>')
def pacchetti(card):
    print(card)
    if card in cards:
        return render_template('card.html', pack=card.capitalize(), desc=cards[card][0], elementi=cards[card][1], img=cards[card][2])
    else:
        return '<h1>Errore</h1>'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
