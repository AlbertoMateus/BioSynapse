# Create English version of HTML file
html_english = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Space Biology AI Gap Analyzer - NASA Space Apps Challenge 2025</title>
    <link rel="stylesheet" href="styles.css">
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
</head>
<body>
    <!-- Header -->
    <header class="header">
        <div class="container">
            <div class="logo">
                <h1>🚀 NASA Space Apps Challenge 2025</h1>
                <h2>Space Biology AI Gap Analyzer</h2>
                <p>Identifying AI opportunities in 607 NASA space biology publications</p>
            </div>
            <div class="status">
                <div class="badge success">✅ Analysis Complete</div>
                <div class="badge warning">⚠️ 97.4% AI Gap Identified</div>
            </div>
        </div>
    </header>

    <!-- Main Content -->
    <main class="main">
        <div class="container">
            
            <!-- Problem Statement -->
            <section class="problem-section">
                <h2>🔍 The Problem Identified</h2>
                <div class="problem-grid">
                    <div class="problem-card critical">
                        <h3>📊 Current Situation</h3>
                        <div class="stat">
                            <span class="number">607</span>
                            <span class="label">NASA Publications</span>
                        </div>
                        <div class="stat">
                            <span class="number">2.6%</span>
                            <span class="label">Using AI/ML</span>
                        </div>
                    </div>
                    <div class="problem-card opportunity">
                        <h3>🎯 Opportunity</h3>
                        <div class="stat">
                            <span class="number">591</span>
                            <span class="label">Publications without AI</span>
                        </div>
                        <div class="stat">
                            <span class="number">97.4%</span>
                            <span class="label">Untapped potential</span>
                        </div>
                    </div>
                    <div class="problem-card impact">
                        <h3>⚡ Potential Impact</h3>
                        <ul>
                            <li>Accelerate scientific discoveries</li>
                            <li>Identify early biomarkers</li>
                            <li>Predict mission risks</li>
                            <li>Optimize countermeasures</li>
                        </ul>
                    </div>
                </div>
            </section>

            <!-- Gap Analysis Dashboard -->
            <section class="dashboard-section">
                <h2>📈 AI Gap Analysis Dashboard</h2>
                
                <!-- Controls -->
                <div class="controls">
                    <input type="text" id="searchInput" placeholder="🔍 Search publications..." class="search-input">
                    <select id="areaFilter" class="filter-select">
                        <option value="">All research areas</option>
                        <option value="bone_muscle">Bone/Muscle (92)</option>
                        <option value="cellular">Cellular (167)</option>
                        <option value="microgravity">Microgravity (199)</option>
                        <option value="radiation">Radiation (64)</option>
                        <option value="cardiovascular">Cardiovascular (28)</option>
                        <option value="immune">Immune (27)</option>
                        <option value="neurological">Neurological (14)</option>
                    </select>
                    <button id="analyzeBtn" class="btn-primary">🤖 Analyze Gaps</button>
                </div>

                <!-- Charts Container -->
                <div class="charts-grid">
                    <div class="chart-container">
                        <h3>AI Gaps by Research Area</h3>
                        <canvas id="gapChart"></canvas>
                    </div>
                    <div class="chart-container">
                        <h3>AI Application Potential</h3>
                        <canvas id="potentialChart"></canvas>
                    </div>
                </div>

                <!-- Gap Details -->
                <div class="gap-details" id="gapDetails">
                    <h3>📋 Identified Gap Details</h3>
                    <div class="gap-cards" id="gapCards">
                        <!-- Will be populated dynamically -->
                    </div>
                </div>
            </section>

            <!-- AI Recommendations -->
            <section class="recommendations-section">
                <h2>🤖 AI Recommendations</h2>
                <div class="recommendations-grid" id="recommendationsGrid">
                    <!-- Will be populated dynamically -->
                </div>
            </section>

            <!-- Publications Explorer -->
            <section class="publications-section">
                <h2>📚 Publications Explorer</h2>
                <div class="publications-table-container">
                    <table class="publications-table" id="publicationsTable">
                        <thead>
                            <tr>
                                <th>Title</th>
                                <th>Research Area</th>
                                <th>Uses AI</th>
                                <th>AI Potential</th>
                                <th>Link</th>
                            </tr>
                        </thead>
                        <tbody id="publicationsBody">
                            <!-- Will be populated dynamically -->
                        </tbody>
                    </table>
                </div>
            </section>

        </div>
    </main>

    <!-- Footer -->
    <footer class="footer">
        <div class="container">
            <p>🚀 NASA Space Apps Challenge 2025 - Space Biology AI Gap Analyzer</p>
            <p>Identifying AI opportunities to accelerate space biology discoveries</p>
        </div>
    </footer>

    <script src="script.js"></script>
</body>
</html>'''

# Save English HTML
with open('index_en.html', 'w', encoding='utf-8') as f:
    f.write(html_english)

print("✅ English HTML file created: index_en.html")