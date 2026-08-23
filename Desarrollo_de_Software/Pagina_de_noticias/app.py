from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)
app.config['SECRET_KEY'] = 'clave_secreta_desarrollo'

# Datos en memoria (sin base de datos)
noticias = [
    {
        'id': 1,
        'titulo': 'Bienvenido a nuestro Diario Digital',
        'subtitulo': 'Espacio de información, debate y opinión pública.',
        'categoria': 'Nacional',
        'contenido': 'Esta es una publicación de prueba para estrenar el portal. Aquí los lectores podrán opinar, dar likes/dislikes y enviar comentarios.',
        'fecha': '25/07/2026 10:00',
        'likes': 3,
        'dislikes': 0,
        'comentarios': [
            {'autor': 'Lector 1', 'contenido': '¡Mucho éxito con la página!', 'fecha': '25/07/2026 10:15'}
        ]
    }
]

@app.route('/')
def index():
    noticias_ordenadas = sorted(noticias, key=lambda x: x['id'], reverse=True)
    return render_template('index.html', noticias=noticias_ordenadas)

@app.route('/noticia/<int:id>')
def articulo(id):
    noticia = next((n for n in noticias if n['id'] == id), None)
    if not noticia:
        return "Noticia no encontrada", 404
    return render_template('articulo.html', noticia=noticia)

@app.route('/crear', methods=['GET', 'POST'])
def crear_noticia():
    if request.method == 'POST':
        nuevo_id = len(noticias) + 1
        nueva_noticia = {
            'id': nuevo_id,
            'titulo': request.form.get('titulo'),
            'subtitulo': request.form.get('subtitulo'),
            'categoria': request.form.get('categoria'),
            'contenido': request.form.get('contenido'),
            'fecha': datetime.now().strftime('%d/%m/%Y %H:%M'),
            'likes': 0,
            'dislikes': 0,
            'comentarios': []
        }
        noticias.append(nueva_noticia)
        return redirect(url_for('index'))
        
    return render_template('crear_noticia.html')

@app.route('/noticia/<int:id>/comentar', methods=['POST'])
def comentar(id):
    noticia = next((n for n in noticias if n['id'] == id), None)
    if noticia:
        autor = request.form.get('autor') or "Anónimo"
        contenido = request.form.get('contenido')
        if contenido:
            noticia['comentarios'].append({
                'autor': autor,
                'contenido': contenido,
                'fecha': datetime.now().strftime('%d/%m/%Y %H:%M')
            })
    return redirect(url_for('articulo', id=id))

@app.route('/noticia/<int:id>/reaccion', methods=['POST'])
def reaccion(id):
    noticia = next((n for n in noticias if n['id'] == id), None)
    if noticia:
        data = request.get_json()
        tipo = data.get('tipo')
        if tipo == 'like':
            noticia['likes'] += 1
        elif tipo == 'dislike':
            noticia['dislikes'] += 1
        return jsonify({'likes': noticia['likes'], 'dislikes': noticia['dislikes']})
    return jsonify({'error': 'Noticia no encontrada'}), 404

if __name__ == '__main__':
    app.run(debug=True)