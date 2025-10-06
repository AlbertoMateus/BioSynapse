# Criar arquivo CSS
css_code = '''/* Reset e Base */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Arial', sans-serif;
    line-height: 1.6;
    color: #333;
    background: linear-gradient(135deg, #0B1426 0%, #1a237e 50%, #283593 100%);
    min-height: 100vh;
}

.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 20px;
}

/* Header */
.header {
    background: rgba(0, 0, 0, 0.3);
    color: white;
    padding: 2rem 0;
    backdrop-filter: blur(10px);
    border-bottom: 2px solid rgba(255, 255, 255, 0.1);
}

.header .container {
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
}

.logo h1 {
    font-size: 2.5rem;
    margin-bottom: 0.5rem;
    background: linear-gradient(45deg, #FFD700, #FFA500);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.logo h2 {
    font-size: 1.8rem;
    color: #E3F2FD;
    margin-bottom: 0.5rem;
}

.logo p {
    font-size: 1rem;
    color: #B3E5FC;
    opacity: 0.9;
}

.status {
    display: flex;
    gap: 1rem;
    flex-wrap: wrap;
}

.badge {
    padding: 0.5rem 1rem;
    border-radius: 20px;
    font-weight: bold;
    font-size: 0.9rem;
}

.badge.success {
    background: #4CAF50;
    color: white;
}

.badge.warning {
    background: #FF9800;
    color: white;
}

/* Main Content */
.main {
    padding: 3rem 0;
}

section {
    background: rgba(255, 255, 255, 0.95);
    margin: 2rem 0;
    padding: 2rem;
    border-radius: 15px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
    backdrop-filter: blur(10px);
}

h2 {
    font-size: 2rem;
    margin-bottom: 1.5rem;
    color: #1565C0;
    border-left: 4px solid #FFD700;
    padding-left: 1rem;
}

/* Problem Section */
.problem-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
    margin-top: 2rem;
}

.problem-card {
    background: white;
    padding: 2rem;
    border-radius: 10px;
    border-left: 5px solid #FFD700;
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
}

.problem-card.critical {
    border-left-color: #F44336;
}

.problem-card.opportunity {
    border-left-color: #4CAF50;
}

.problem-card.impact {
    border-left-color: #FF9800;
}

.problem-card h3 {
    font-size: 1.3rem;
    margin-bottom: 1rem;
    color: #1565C0;
}

.stat {
    margin-bottom: 1rem;
}

.stat .number {
    font-size: 2.5rem;
    font-weight: bold;
    color: #1565C0;
    display: block;
}

.stat .label {
    font-size: 1rem;
    color: #666;
}

.problem-card ul {
    list-style: none;
}

.problem-card li {
    padding: 0.5rem 0;
    border-bottom: 1px solid #eee;
}

.problem-card li:before {
    content: "✓ ";
    color: #4CAF50;
    font-weight: bold;
}

/* Dashboard Section */
.controls {
    display: flex;
    gap: 1rem;
    margin-bottom: 2rem;
    flex-wrap: wrap;
}

.search-input, .filter-select {
    padding: 1rem;
    border: 2px solid #E3F2FD;
    border-radius: 8px;
    font-size: 1rem;
    flex: 1;
    min-width: 200px;
}

.search-input:focus, .filter-select:focus {
    outline: none;
    border-color: #1565C0;
}

.btn-primary {
    background: linear-gradient(135deg, #1565C0, #0D47A1);
    color: white;
    border: none;
    padding: 1rem 2rem;
    border-radius: 8px;
    font-size: 1rem;
    cursor: pointer;
    transition: all 0.3s ease;
}

.btn-primary:hover {
    transform: translateY(-2px);
    box-shadow: 0 5px 15px rgba(21, 101, 192, 0.3);
}

.charts-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
    gap: 2rem;
    margin: 2rem 0;
}

.chart-container {
    background: white;
    padding: 1.5rem;
    border-radius: 10px;
    box-shadow: 0 3px 10px rgba(0, 0, 0, 0.1);
}

.chart-container h3 {
    margin-bottom: 1rem;
    text-align: center;
    color: #1565C0;
}

canvas {
    max-height: 400px;
}

/* Gap Details */
.gap-cards {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 1.5rem;
    margin-top: 1.5rem;
}

.gap-card {
    background: linear-gradient(135deg, #E3F2FD, #BBDEFB);
    padding: 1.5rem;
    border-radius: 10px;
    border-left: 4px solid #1565C0;
}

.gap-card h4 {
    color: #0D47A1;
    margin-bottom: 1rem;
    font-size: 1.2rem;
}

.gap-stat {
    display: flex;
    justify-content: space-between;
    margin-bottom: 0.5rem;
    font-size: 0.9rem;
}

.gap-stat .value {
    font-weight: bold;
    color: #1565C0;
}

/* Recommendations Section */
.recommendations-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
    gap: 2rem;
}

.recommendation-card {
    background: linear-gradient(135deg, #F3E5F5, #E1BEE7);
    padding: 1.5rem;
    border-radius: 10px;
    border-left: 4px solid #9C27B0;
}

.recommendation-card h4 {
    color: #6A1B9A;
    margin-bottom: 1rem;
    font-size: 1.2rem;
}

.ai-technique {
    background: rgba(156, 39, 176, 0.1);
    padding: 0.5rem;
    border-radius: 5px;
    margin: 0.5rem 0;
    font-size: 0.9rem;
}

/* Publications Table */
.publications-table-container {
    overflow-x: auto;
    margin-top: 1rem;
}

.publications-table {
    width: 100%;
    border-collapse: collapse;
    background: white;
}

.publications-table th,
.publications-table td {
    padding: 1rem;
    text-align: left;
    border-bottom: 1px solid #ddd;
}

.publications-table th {
    background: #1565C0;
    color: white;
    font-weight: bold;
}

.publications-table tr:hover {
    background: #f5f5f5;
}

.ai-status {
    padding: 0.3rem 0.8rem;
    border-radius: 15px;
    font-size: 0.8rem;
    font-weight: bold;
    text-align: center;
}

.ai-status.yes {
    background: #4CAF50;
    color: white;
}

.ai-status.no {
    background: #F44336;
    color: white;
}

.potential-score {
    padding: 0.3rem 0.8rem;
    border-radius: 15px;
    font-size: 0.8rem;
    font-weight: bold;
    text-align: center;
    background: #FF9800;
    color: white;
}

.pub-link {
    color: #1565C0;
    text-decoration: none;
    font-weight: bold;
}

.pub-link:hover {
    text-decoration: underline;
}

/* Footer */
.footer {
    background: rgba(0, 0, 0, 0.8);
    color: white;
    text-align: center;
    padding: 2rem 0;
    margin-top: 3rem;
}

/* Responsive Design */
@media (max-width: 768px) {
    .header .container {
        flex-direction: column;
        text-align: center;
    }

    .logo h1 {
        font-size: 2rem;
    }

    .logo h2 {
        font-size: 1.5rem;
    }

    .controls {
        flex-direction: column;
    }

    .charts-grid {
        grid-template-columns: 1fr;
    }

    .problem-grid,
    .gap-cards,
    .recommendations-grid {
        grid-template-columns: 1fr;
    }
}

/* Animations */
@keyframes fadeIn {
    from {
        opacity: 0;
        transform: translateY(20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

section {
    animation: fadeIn 0.6s ease-out;
}

.gap-card,
.recommendation-card,
.problem-card {
    transition: transform 0.3s ease;
}

.gap-card:hover,
.recommendation-card:hover,
.problem-card:hover {
    transform: translateY(-5px);
}

/* Loading State */
.loading {
    text-align: center;
    padding: 2rem;
    color: #666;
}

.loading:before {
    content: "⏳ ";
    font-size: 1.5rem;
}'''

# Salvar CSS
with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css_code)

print("✅ Arquivo CSS criado: styles.css")