from flask import Flask, request, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)
# Serve static files from public directory
@app.route('/')
def root():
    return send_from_directory('public', 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('public', path)

# Handle snapshot POST requests
@app.route('/snapshot', methods=['POST'])
def save_snapshot():
    html_content = request.data.decode('utf-8')
    
    # Create snapshots directory if it doesn't exist
    snapshots_dir = os.path.join('public', 'snapshots')
    os.makedirs(snapshots_dir, exist_ok=True)
    
    # Find the next available snapshot number
    existing_snapshots = [f for f in os.listdir(snapshots_dir) 
                         if f.startswith('snapshot_') and f.endswith('.html')]
    
    if existing_snapshots:
        numbers = [int(f.replace('snapshot_', '').replace('.html', '')) 
                  for f in existing_snapshots]
        next_number = max(numbers) + 1
    else:
        next_number = 1
    
    # Save the new snapshot
    filename = f'snapshot_{next_number}.html'
    filepath = os.path.join(snapshots_dir, filename)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    return {'status': 'success', 'filename': filename}, 200

if __name__ == '__main__':
    app.run(debug=True, port=8000)
