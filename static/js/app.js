// Career Guidance Agent - Professional JavaScript

// Specialization options based on field selection
const specializationOptions = {
    tech: [
        { value: 'frontend', text: 'Frontend Development' },
        { value: 'backend', text: 'Backend Development' },
        { value: 'data_science', text: 'Data Science' },
        { value: 'devops', text: 'DevOps' },
        { value: 'mobile', text: 'Mobile Development' },
        { value: 'cybersecurity', text: 'Cybersecurity' },
        { value: 'ai_ml', text: 'AI/ML Engineering' }
    ],
    mba: [
        { value: 'consulting', text: 'Management Consulting' },
        { value: 'finance', text: 'Finance & Investment Banking' },
        { value: 'marketing', text: 'Marketing Consultant' },
        { value: 'operations', text: 'Operations & Supply Chain' },
        { value: 'strategy', text: 'Corporate Strategy' },
        { value: 'entrepreneurship', text: 'Entrepreneurship' },
        { value: 'hr', text: 'Human Resources' }
    ]
};

// Global state for storing loaded guides
let managementConsultingGuide = null;
let marketingConsultantRoadmap = null;

// Initialize the application
document.addEventListener('DOMContentLoaded', function() {
    initializeApp();
});

function initializeApp() {
    setupFieldChangeHandler();
    setupFormSubmission();
    setupSmoothScrolling();
    setupAnimations();
}

// Handle field selection change
function setupFieldChangeHandler() {
    const fieldSelect = document.getElementById('field');
    const specializationSelect = document.getElementById('specialization');
    
    fieldSelect.addEventListener('change', function() {
        const selectedField = this.value;
        updateSpecializationOptions(selectedField, specializationSelect);
    });
}

function updateSpecializationOptions(field, selectElement) {
    // Clear existing options
    selectElement.innerHTML = '<option value="">Select specialization (optional)</option>';
    
    if (field && specializationOptions[field]) {
        specializationOptions[field].forEach(option => {
            const optionElement = document.createElement('option');
            optionElement.value = option.value;
            optionElement.textContent = option.text;
            selectElement.appendChild(optionElement);
        });
    }
}

// Handle form submission
function setupFormSubmission() {
    const form = document.getElementById('careerForm');
    
    form.addEventListener('submit', async function(e) {
        e.preventDefault();
        
        const formData = new FormData(form);
        const queryData = {
            field: formData.get('field'),
            specialization: formData.get('specialization') || null,
            experience_level: formData.get('experience_level'),
            location_preference: formData.get('location_preference') || null,
            target_companies: formData.get('target_companies') ? 
                formData.get('target_companies').split(',').map(c => c.trim()) : null,
            target_roles: formData.get('target_roles') ? 
                formData.get('target_roles').split(',').map(r => r.trim()) : null,
            skills: formData.get('skills') ? 
                formData.get('skills').split(',').map(s => s.trim()) : null,
            query_text: formData.get('query_text')
        };
        
        await submitCareerQuery(queryData);
    });
}

async function submitCareerQuery(queryData) {
    try {
        // Show loading spinner
        showLoadingSpinner();
        
        // Submit the query
        const response = await fetch('/api/career-guidance', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(queryData)
        });
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const result = await response.json();
        
        // Hide loading spinner
        hideLoadingSpinner();
        
        // Display results
        displayResults(result);
        
        // Scroll to results
        document.getElementById('resultsSection').scrollIntoView({ 
            behavior: 'smooth' 
        });
        
    } catch (error) {
        console.error('Error submitting career query:', error);
        hideLoadingSpinner();
        showError('Failed to generate career roadmap. Please try again.');
    }
}

function showLoadingSpinner() {
    document.getElementById('loadingSpinner').style.display = 'block';
    document.getElementById('resultsSection').style.display = 'none';
}

function hideLoadingSpinner() {
    document.getElementById('loadingSpinner').style.display = 'none';
}

function showError(message) {
    const resultsSection = document.getElementById('resultsSection');
    resultsSection.innerHTML = `
        <div class="container">
            <div class="alert alert-danger" role="alert">
                <i class="fas fa-exclamation-triangle me-2"></i>
                ${message}
            </div>
        </div>
    `;
    resultsSection.style.display = 'block';
}

function displayResults(result) {
    const resultsSection = document.getElementById('resultsSection');
    
    resultsSection.innerHTML = `
        <div class="container">
            <div class="row">
                <div class="col-12">
                    <div class="text-center mb-5">
                        <h2 class="display-5 fw-bold text-gradient">
                            <i class="fas fa-compass me-2"></i>
                            Your Career Roadmap
                        </h2>
                        <p class="lead text-muted">Personalized guidance for your career journey</p>
                    </div>
                </div>
            </div>
            
            ${generateRoadmapSection(result.roadmap)}
            ${generateMarketDataSection(result.market_data)}
            ${generateMarketTrendsSection(result.market_trends)}
            ${generateLayoffStatsSection(result.layoff_statistics)}
            ${generateSkillRequirementsSection(result.skill_requirements)}
            ${generateRecommendationsSection(result.recommendations)}
        </div>
    `;
    
    resultsSection.style.display = 'block';
    resultsSection.classList.add('fade-in');
}

function generateRoadmapSection(roadmap) {
    if (!roadmap) return '';
    
    return `
        <div class="row mb-5">
            <div class="col-12">
                <div class="result-card">
                    <h3 class="mb-4">
                        <i class="fas fa-route me-2 text-primary"></i>
                        Learning Roadmap - ${roadmap.specialization.charAt(0).toUpperCase() + roadmap.specialization.slice(1)}
                    </h3>
                    <p class="text-muted mb-4">
                        <i class="fas fa-clock me-2"></i>
                        Estimated Duration: ${roadmap.total_duration}
                    </p>
                    
                    <div class="row">
                        ${roadmap.steps.map((step, index) => `
                            <div class="col-lg-6 mb-3">
                                <div class="roadmap-step">
                                    <div class="d-flex align-items-start">
                                        <div class="step-number">${index + 1}</div>
                                        <div class="flex-grow-1">
                                            <h5 class="mb-2">${step.title}</h5>
                                            <p class="text-muted mb-2">${step.description}</p>
                                            <div class="mb-2">
                                                <span class="badge bg-primary me-2">
                                                    <i class="fas fa-clock me-1"></i>
                                                    ${step.duration}
                                                </span>
                                                <span class="badge bg-secondary">
                                                    <i class="fas fa-signal me-1"></i>
                                                    ${step.difficulty}
                                                </span>
                                            </div>
                                            <div class="mb-2">
                                                <strong>Resources:</strong>
                                                <div class="mt-1">
                                                    ${step.resources.map(resource => 
                                                        `<span class="skill-tag">${resource}</span>`
                                                    ).join('')}
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        `).join('')}
                    </div>
                    
                    <div class="mt-4">
                        <h5>Skills You'll Master:</h5>
                        <div class="mt-2">
                            ${roadmap.skills_covered.map(skill => 
                                `<span class="skill-tag">${skill}</span>`
                            ).join('')}
                        </div>
                    </div>
                </div>
            </div>
        </div>
    `;
}

function generateMarketDataSection(marketData) {
    if (!marketData || marketData.length === 0) return '';
    
    return `
        <div class="row mb-5">
            <div class="col-12">
                <div class="result-card">
                    <h3 class="mb-4">
                        <i class="fas fa-chart-bar me-2 text-primary"></i>
                        Company Market Data
                    </h3>
                    <div class="row">
                        ${marketData.map(company => `
                            <div class="col-lg-4 col-md-6 mb-3">
                                <div class="company-card">
                                    <h5 class="mb-2">${company.name}</h5>
                                    <p class="text-muted mb-2">
                                        <i class="fas fa-building me-2"></i>
                                        ${company.industry} • ${company.company_size}
                                    </p>
                                    <div class="mb-2">
                                        <span class="badge ${company.hiring_status === 'Active' ? 'bg-success' : 'bg-warning'}">
                                            ${company.hiring_status} Hiring
                                        </span>
                                    </div>
                                    <p class="mb-2">
                                        <strong>Open Positions:</strong> ${company.open_positions}
                                    </p>
                                    ${company.average_salary ? `
                                        <p class="mb-2">
                                            <strong>Avg Salary:</strong> $${company.average_salary.toLocaleString()}
                                        </p>
                                    ` : ''}
                                    <div>
                                        <strong>Key Skills:</strong>
                                        <div class="mt-1">
                                            ${company.required_skills.map(skill => 
                                                `<span class="skill-tag">${skill}</span>`
                                            ).join('')}
                                        </div>
                                    </div>
                                </div>
                            </div>
                        `).join('')}
                    </div>
                </div>
            </div>
        </div>
    `;
}

function generateMarketTrendsSection(marketTrends) {
    if (!marketTrends || marketTrends.length === 0) return '';
    
    return `
        <div class="row mb-5">
            <div class="col-12">
                <div class="result-card">
                    <h3 class="mb-4">
                        <i class="fas fa-trending-up me-2 text-primary"></i>
                        Market Trends
                    </h3>
                    <div class="row">
                        ${marketTrends.map(trend => `
                            <div class="col-lg-6 mb-3">
                                <div class="trend-card">
                                    <h5 class="mb-2">${trend.trend_type}</h5>
                                    <p class="mb-2">${trend.description}</p>
                                    <div class="d-flex justify-content-between align-items-center">
                                        <span class="badge ${trend.impact === 'High' ? 'bg-warning' : 'bg-info'}">
                                            ${trend.impact} Impact
                                        </span>
                                        <small>${trend.timeframe}</small>
                                    </div>
                                    <small class="d-block mt-2 opacity-75">Source: ${trend.source}</small>
                                </div>
                            </div>
                        `).join('')}
                    </div>
                </div>
            </div>
        </div>
    `;
}

function generateLayoffStatsSection(layoffStats) {
    if (!layoffStats || layoffStats.length === 0) return '';
    
    return `
        <div class="row mb-5">
            <div class="col-12">
                <div class="result-card">
                    <h3 class="mb-4">
                        <i class="fas fa-exclamation-triangle me-2 text-warning"></i>
                        Recent Layoff Statistics
                    </h3>
                    <div class="row">
                        ${layoffStats.map(layoff => `
                            <div class="col-lg-4 col-md-6 mb-3">
                                <div class="company-card border-warning">
                                    <h5 class="mb-2 text-warning">${layoff.company}</h5>
                                    <p class="mb-2">
                                        <strong>Layoffs:</strong> ${layoff.layoff_count.toLocaleString()} employees
                                    </p>
                                    <p class="mb-2">
                                        <strong>Percentage:</strong> ${layoff.percentage}%
                                    </p>
                                    <p class="mb-2">
                                        <strong>Date:</strong> ${new Date(layoff.date).toLocaleDateString()}
                                    </p>
                                    <p class="mb-2">
                                        <strong>Reason:</strong> ${layoff.reason}
                                    </p>
                                    <div>
                                        <strong>Affected Departments:</strong>
                                        <div class="mt-1">
                                            ${layoff.affected_departments.map(dept => 
                                                `<span class="skill-tag bg-warning">${dept}</span>`
                                            ).join('')}
                                        </div>
                                    </div>
                                </div>
                            </div>
                        `).join('')}
                    </div>
                </div>
            </div>
        </div>
    `;
}

function generateSkillRequirementsSection(skillRequirements) {
    if (!skillRequirements || skillRequirements.length === 0) return '';
    
    return `
        <div class="row mb-5">
            <div class="col-12">
                <div class="result-card">
                    <h3 class="mb-4">
                        <i class="fas fa-tools me-2 text-primary"></i>
                        Skill Requirements
                    </h3>
                    <div class="row">
                        ${skillRequirements.map(skills => `
                            <div class="col-lg-6 mb-4">
                                <div class="company-card">
                                    <h5 class="mb-3">${skills.role}</h5>
                                    
                                    <div class="mb-3">
                                        <h6 class="text-success">Essential Skills:</h6>
                                        <div class="mt-1">
                                            ${skills.essential_skills.map(skill => 
                                                `<span class="skill-tag bg-success">${skill}</span>`
                                            ).join('')}
                                        </div>
                                    </div>
                                    
                                    <div class="mb-3">
                                        <h6 class="text-info">Nice to Have:</h6>
                                        <div class="mt-1">
                                            ${skills.nice_to_have_skills.map(skill => 
                                                `<span class="skill-tag bg-info">${skill}</span>`
                                            ).join('')}
                                        </div>
                                    </div>
                                    
                                    <p class="mb-2">
                                        <strong>Experience Required:</strong> ${skills.experience_required}
                                    </p>
                                    
                                    ${skills.certifications.length > 0 ? `
                                        <div>
                                            <strong>Certifications:</strong>
                                            <div class="mt-1">
                                                ${skills.certifications.map(cert => 
                                                    `<span class="skill-tag bg-secondary">${cert}</span>`
                                                ).join('')}
                                            </div>
                                        </div>
                                    ` : ''}
                                </div>
                            </div>
                        `).join('')}
                    </div>
                </div>
            </div>
        </div>
    `;
}

function generateRecommendationsSection(recommendations) {
    if (!recommendations || recommendations.length === 0) return '';
    
    return `
        <div class="row mb-5">
            <div class="col-12">
                <div class="result-card">
                    <h3 class="mb-4">
                        <i class="fas fa-lightbulb me-2 text-warning"></i>
                        Personalized Recommendations
                    </h3>
                    <div class="row">
                        <div class="col-12">
                            ${recommendations.map((recommendation, index) => `
                                <div class="recommendation-item">
                                    <div class="d-flex align-items-start">
                                        <div class="me-3">
                                            <i class="fas fa-check-circle text-success"></i>
                                        </div>
                                        <div>
                                            <p class="mb-0">${recommendation}</p>
                                        </div>
                                    </div>
                                </div>
                            `).join('')}
                        </div>
                    </div>
                </div>
            </div>
        </div>
    `;
}

// Smooth scrolling functions
function setupSmoothScrolling() {
    // Smooth scroll for navigation links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
}

function scrollToForm() {
    document.getElementById('guidance-form').scrollIntoView({ 
        behavior: 'smooth' 
    });
}

function scrollToFeatures() {
    document.getElementById('features').scrollIntoView({ 
        behavior: 'smooth' 
    });
}

// Setup animations
function setupAnimations() {
    // Intersection Observer for fade-in animations
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in');
            }
        });
    }, observerOptions);
    
    // Observe elements for animation
    document.querySelectorAll('.feature-card, .result-card').forEach(el => {
        observer.observe(el);
    });
}

// Utility functions
function formatCurrency(amount) {
    return new Intl.NumberFormat('en-US', {
        style: 'currency',
        currency: 'USD',
        minimumFractionDigits: 0,
        maximumFractionDigits: 0
    }).format(amount);
}

function formatDate(dateString) {
    return new Date(dateString).toLocaleDateString('en-US', {
        year: 'numeric',
        month: 'long',
        day: 'numeric'
    });
}

// Load Management Consulting Guide
async function loadManagementConsultingGuide() {
    try {
        showLoading();
        const response = await fetch('/api/management-consulting-guide');
        if (!response.ok) throw new Error('Failed to load guide');
        
        const guide = await response.json();
        managementConsultingGuide = guide;
        displayManagementConsultingGuide(guide);
    } catch (error) {
        console.error('Error loading management consulting guide:', error);
        showError('Failed to load management consulting guide');
    } finally {
        hideLoading();
    }
}

// Display Management Consulting Guide
function displayManagementConsultingGuide(guide) {
    const resultsDiv = document.getElementById('results');
    resultsDiv.style.display = 'block';
    resultsDiv.scrollIntoView({ behavior: 'smooth' });
    
    // Clear existing content
    document.getElementById('roadmapContent').innerHTML = '';
    document.getElementById('skillsContent').innerHTML = '';
    document.getElementById('marketContent').innerHTML = '';
    document.getElementById('recommendationsContent').innerHTML = '';
    
    // Display skills breakdown
    const skillsContent = document.getElementById('skillsContent');
    skillsContent.innerHTML = `
        <h4 class="mb-3">🔧 Top Skills Sought by Indian Employers</h4>
        <div class="row">
            ${Object.values(guide.skills_breakdown).map(skill => `
                <div class="col-md-6 mb-3">
                    <div class="card border-0 bg-light">
                        <div class="card-body">
                            <h6 class="card-title">${skill.title}</h6>
                            <p class="card-text small">${skill.description}</p>
                            <div class="mt-2">
                                ${skill.key_skills.map(s => `<span class="skill-tag">${s}</span>`).join('')}
                            </div>
                        </div>
                    </div>
                </div>
            `).join('')}
        </div>
    `;
    
    // Display learning resources
    const marketContent = document.getElementById('marketContent');
    marketContent.innerHTML = `
        <h4 class="mb-3">📚 Learning Resources</h4>
        <div class="row">
            <div class="col-md-6 mb-3">
                <h6>Case Interview Preparation</h6>
                <ul class="list-group list-group-flush">
                    ${guide.learning_resources.case_interview_prep.map(resource => `
                        <li class="list-group-item d-flex justify-content-between align-items-center">
                            <div>
                                <strong>${resource.resource}</strong>
                                <br><small class="text-muted">${resource.description}</small>
                            </div>
                            <span class="badge bg-primary">${resource.type}</span>
                        </li>
                    `).join('')}
                </ul>
            </div>
            <div class="col-md-6 mb-3">
                <h6>Business & Industry Awareness</h6>
                <ul class="list-group list-group-flush">
                    ${guide.learning_resources.business_industry_awareness.map(resource => `
                        <li class="list-group-item d-flex justify-content-between align-items-center">
                            <div>
                                <strong>${resource.resource}</strong>
                                <br><small class="text-muted">${resource.description}</small>
                            </div>
                            <span class="badge bg-secondary">${resource.type}</span>
                        </li>
                    `).join('')}
                </ul>
            </div>
        </div>
    `;
    
    // Display success tips
    const recommendationsContent = document.getElementById('recommendationsContent');
    recommendationsContent.innerHTML = `
        <h4 class="mb-3">💡 Success Tips</h4>
        <div class="row">
            ${guide.success_tips.map(tip => `
                <div class="col-md-6 mb-2">
                    <div class="recommendation-item">
                        <i class="fas fa-check-circle text-success me-2"></i>
                        ${tip}
                    </div>
                </div>
            `).join('')}
        </div>
    `;
}

// Load Marketing Consultant Roadmap
async function loadMarketingConsultantRoadmap() {
    try {
        showLoading();
        const response = await fetch('/api/marketing-consultant-roadmap');
        if (!response.ok) throw new Error('Failed to load roadmap');
        
        const roadmap = await response.json();
        marketingConsultantRoadmap = roadmap;
        displayMarketingConsultantRoadmap(roadmap);
    } catch (error) {
        console.error('Error loading marketing consultant roadmap:', error);
        showError('Failed to load marketing consultant roadmap');
    } finally {
        hideLoading();
    }
}

// Display Marketing Consultant Roadmap
function displayMarketingConsultantRoadmap(roadmap) {
    const resultsDiv = document.getElementById('results');
    resultsDiv.style.display = 'block';
    resultsDiv.scrollIntoView({ behavior: 'smooth' });
    
    // Clear existing content
    document.getElementById('roadmapContent').innerHTML = '';
    document.getElementById('skillsContent').innerHTML = '';
    document.getElementById('marketContent').innerHTML = '';
    document.getElementById('recommendationsContent').innerHTML = '';
    
    // Display roadmap steps
    const roadmapContent = document.getElementById('roadmapContent');
    roadmapContent.innerHTML = `
        <div class="mb-3">
            <h4>🎯 ${roadmap.title}</h4>
            <p class="text-muted">${roadmap.description}</p>
            <div class="row mb-4">
                <div class="col-md-4">
                    <div class="text-center p-3 bg-light rounded">
                        <h6 class="text-primary">Timeline</h6>
                        <p class="mb-0">${roadmap.timeline}</p>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="text-center p-3 bg-light rounded">
                        <h6 class="text-primary">Target Companies</h6>
                        <p class="mb-0">${roadmap.target_companies.length} firms</p>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="text-center p-3 bg-light rounded">
                        <h6 class="text-primary">Key Skills</h6>
                        <p class="mb-0">${roadmap.key_skills.length} skills</p>
                    </div>
                </div>
            </div>
        </div>
        <h5 class="mb-3">📅 Month-by-Month Breakdown</h5>
        ${roadmap.monthly_breakdown.map(month => `
            <div class="roadmap-step">
                <div class="d-flex align-items-start">
                    <div class="step-number">${month.month}</div>
                    <div class="flex-grow-1">
                        <h6 class="mb-2">${month.focus_area}</h6>
                        <p class="mb-2">${month.description}</p>
                        <div class="row">
                            <div class="col-md-6">
                                <strong>Actions:</strong>
                                <ul class="mb-0">
                                    ${month.actions.map(action => `<li>${action}</li>`).join('')}
                                </ul>
                            </div>
                            <div class="col-md-6">
                                <strong>Key Skills:</strong>
                                <div class="mt-1">
                                    ${month.key_skills.map(skill => `<span class="skill-tag">${skill}</span>`).join('')}
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        `).join('')}
    `;
    
    // Display skills and certifications
    const skillsContent = document.getElementById('skillsContent');
    skillsContent.innerHTML = `
        <div class="row">
            <div class="col-md-6">
                <h5>🔑 Key Skills</h5>
                <div class="mb-3">
                    ${roadmap.key_skills.map(skill => `<span class="skill-tag">${skill}</span>`).join('')}
                </div>
            </div>
            <div class="col-md-6">
                <h5>📜 Certifications</h5>
                <ul class="list-group list-group-flush">
                    ${roadmap.certifications.map(cert => `
                        <li class="list-group-item">${cert}</li>
                    `).join('')}
                </ul>
            </div>
        </div>
    `;
    
    // Display target companies
    const marketContent = document.getElementById('marketContent');
    marketContent.innerHTML = `
        <h5>🏢 Target Companies</h5>
        <div class="row">
            ${roadmap.target_companies.map(company => `
                <div class="col-md-4 mb-2">
                    <div class="company-card">
                        <strong>${company}</strong>
                    </div>
                </div>
            `).join('')}
        </div>
    `;
    
    // Display success tips
    const recommendationsContent = document.getElementById('recommendationsContent');
    recommendationsContent.innerHTML = `
        <h5>💡 Success Tips</h5>
        <div class="row">
            ${roadmap.success_tips.map(tip => `
                <div class="col-md-6 mb-2">
                    <div class="recommendation-item">
                        <i class="fas fa-lightbulb text-warning me-2"></i>
                        ${tip}
                    </div>
                </div>
            `).join('')}
        </div>
    `;
}

// Export functions for global access
window.scrollToForm = scrollToForm;
window.scrollToFeatures = scrollToFeatures;
window.loadManagementConsultingGuide = loadManagementConsultingGuide;
window.loadMarketingConsultantRoadmap = loadMarketingConsultantRoadmap;
