"""
Developer Experience (DevEx) Module - AI Enhanced
Comprehensive developer tools, documentation, and AI assistance
"""

import streamlit as st
import json
import os
from typing import Dict, List, Optional

# ============================================================================
# AI CLIENT
# ============================================================================

@st.cache_resource
def get_anthropic_client():
    """Initialize and cache Anthropic client"""
    api_key = None
    
    if hasattr(st, 'secrets'):
        try:
            if 'anthropic' in st.secrets and 'api_key' in st.secrets['anthropic']:
                api_key = st.secrets['anthropic']['api_key']
        except:
            pass
    
    if not api_key and hasattr(st, 'secrets') and 'ANTHROPIC_API_KEY' in st.secrets:
        api_key = st.secrets['ANTHROPIC_API_KEY']
    
    if not api_key:
        api_key = os.environ.get('ANTHROPIC_API_KEY')
    
    if not api_key:
        return None
    
    try:
        import anthropic
        return anthropic.Anthropic(api_key=api_key)
    except Exception as e:
        return None

# ============================================================================
# MAIN MODULE
# ============================================================================

class DevExModule:
    """Developer Experience - AI Enhanced"""
    
    @staticmethod
    def render():
        """Render Developer Experience module"""
        st.title("👨‍💻 Developer Experience (DevEx)")
        st.caption("🤖 AI-powered tools, documentation, and code assistance for CloudIDP developers")
        
        # AI availability
        ai_available = get_anthropic_client() is not None
        
        if ai_available:
            st.success("🤖 **AI Code Assistant: ENABLED** | Get instant code help | Generate snippets | Debug issues")
        else:
            st.info("💡 Enable AI features by configuring ANTHROPIC_API_KEY in secrets")
        
        # Main tabs
        tabs = st.tabs([
            "🏠 Developer Portal",
            "📚 API Documentation",
            "💻 Code Samples",
            "🔧 SDK & CLI Tools",
            "🚀 Quick Start",
            "🎯 Sandbox Environment",
            "🤖 AI Code Assistant",
            "🐛 Troubleshooting"
        ])
        
        with tabs[0]:
            DevExModule._render_developer_portal()
        
        with tabs[1]:
            DevExModule._render_api_documentation()
        
        with tabs[2]:
            DevExModule._render_code_samples()
        
        with tabs[3]:
            DevExModule._render_sdk_cli_tools()
        
        with tabs[4]:
            DevExModule._render_quick_start()
        
        with tabs[5]:
            DevExModule._render_sandbox()
        
        with tabs[6]:
            DevExModule._render_ai_code_assistant(ai_available)
        
        with tabs[7]:
            DevExModule._render_troubleshooting(ai_available)
    
    # ========================================================================
    # TAB 1: DEVELOPER PORTAL
    # ========================================================================
    
    @staticmethod
    def _render_developer_portal():
        """Developer portal home"""
        st.subheader("🏠 CloudIDP Developer Portal")
        
        st.markdown("""
        ### Welcome to CloudIDP Developer Center!
        
        Everything you need to integrate with CloudIDP and build amazing cloud solutions.
        """)
        
        # Quick links
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
            ### 🚀 Getting Started
            - [Quick Start Guide](#)
            - [Authentication Setup](#)
            - [First API Call](#)
            - [Sample Projects](#)
            """)
        
        with col2:
            st.markdown("""
            ### 📚 Documentation
            - [API Reference](#)
            - [SDK Documentation](#)
            - [Code Samples](#)
            - [Best Practices](#)
            """)
        
        with col3:
            st.markdown("""
            ### 🛠️ Developer Tools
            - [API Explorer](#)
            - [SDK Downloads](#)
            - [CLI Tools](#)
            - [Sandbox Access](#)
            """)
        
        st.markdown("---")
        
        # Popular resources
        st.markdown("### 📖 Popular Resources")
        
        resources = [
            {"Title": "CloudIDP Python SDK", "Type": "SDK", "Downloads": "12.5K", "Link": "View"},
            {"Title": "Account Provisioning API", "Type": "API", "Views": "45.2K", "Link": "View"},
            {"Title": "Multi-Account Setup Guide", "Type": "Tutorial", "Views": "8.9K", "Link": "View"},
            {"Title": "Security Best Practices", "Type": "Guide", "Views": "15.3K", "Link": "View"}
        ]
        
        import pandas as pd
        df = pd.DataFrame(resources)
        st.dataframe(df, use_container_width=True)
        
        st.markdown("---")
        
        # What's new
        st.markdown("### 🆕 What's New")
        
        st.info("""
        **Latest Updates (December 2024):**
        - 🎉 New AI Code Assistant with Claude integration
        - 🚀 Python SDK v2.0 released with async support
        - 📚 Updated API documentation with interactive examples
        - 🔧 CLI tool now supports batch operations
        """)
    
    # ========================================================================
    # TAB 2: API DOCUMENTATION
    # ========================================================================
    
    @staticmethod
    def _render_api_documentation():
        """API documentation and reference"""
        st.subheader("📚 API Documentation")
        
        st.markdown("### CloudIDP REST API v2.0")
        
        # API categories
        api_category = st.selectbox("Select API Category", [
            "Accounts",
            "Organizations",
            "Security",
            "Network",
            "Resources",
            "FinOps",
            "Provisioning"
        ])
        
        if api_category == "Accounts":
            st.markdown("""
            ### Account Management API
            
            Manage AWS accounts, credentials, and configurations.
            
            **Base URL:** `https://api.cloudidp.com/v2`
            """)
            
            # Example endpoint
            with st.expander("📍 GET /accounts - List all accounts"):
                st.markdown("""
                **Description:** Retrieve a list of all AWS accounts.
                
                **Authentication:** Bearer Token required
                
                **Request:**
                ```bash
                curl -X GET https://api.cloudidp.com/v2/accounts \\
                  -H "Authorization: Bearer YOUR_API_TOKEN" \\
                  -H "Content-Type: application/json"
                ```
                
                **Response (200 OK):**
                ```json
                {
                  "accounts": [
                    {
                      "id": "123456789012",
                      "name": "prod-account-1",
                      "status": "active",
                      "environment": "production",
                      "created_at": "2024-01-15T10:30:00Z"
                    }
                  ],
                  "total": 48,
                  "page": 1
                }
                ```
                
                **Try it now:**
                """)
                
                if st.button("🚀 Test API Call"):
                    st.json({
                        "accounts": [
                            {
                                "id": "123456789012",
                                "name": "prod-account-1",
                                "status": "active",
                                "environment": "production"
                            }
                        ],
                        "total": 48
                    })
            
            with st.expander("📍 POST /accounts - Create new account"):
                st.markdown("""
                **Description:** Create a new AWS account.
                
                **Request:**
                ```bash
                curl -X POST https://api.cloudidp.com/v2/accounts \\
                  -H "Authorization: Bearer YOUR_API_TOKEN" \\
                  -H "Content-Type: application/json" \\
                  -d '{
                    "name": "dev-new-account",
                    "email": "aws+dev@company.com",
                    "environment": "development",
                    "template": "baseline"
                  }'
                ```
                
                **Response (201 Created):**
                ```json
                {
                  "id": "234567890123",
                  "name": "dev-new-account",
                  "status": "provisioning",
                  "message": "Account creation initiated"
                }
                ```
                """)
    
    # ========================================================================
    # TAB 3: CODE SAMPLES
    # ========================================================================
    
    @staticmethod
    def _render_code_samples():
        """Code samples and snippets"""
        st.subheader("💻 Code Samples")
        
        language = st.selectbox("Programming Language", [
            "Python",
            "JavaScript (Node.js)",
            "Bash/Shell",
            "Go",
            "Java"
        ])
        
        use_case = st.selectbox("Use Case", [
            "List Accounts",
            "Create Account",
            "Provision Resources",
            "Security Scan",
            "Cost Analysis",
            "Batch Operations"
        ])
        
        st.markdown("---")
        
        if language == "Python" and use_case == "List Accounts":
            st.markdown("### Python: List All Accounts")
            
            code = '''import requests

# CloudIDP API Configuration
API_BASE = "https://api.cloudidp.com/v2"
API_TOKEN = "your_api_token_here"

# Set headers
headers = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json"
}

# Get all accounts
response = requests.get(f"{API_BASE}/accounts", headers=headers)

if response.status_code == 200:
    accounts = response.json()["accounts"]
    
    for account in accounts:
        print(f"Account: {account['name']} ({account['id']})")
        print(f"  Status: {account['status']}")
        print(f"  Environment: {account['environment']}")
        print()
else:
    print(f"Error: {response.status_code}")
    print(response.text)
'''
            
            st.code(code, language="python")
            
            if st.button("📋 Copy Code"):
                st.success("Code copied to clipboard!")
        
        elif language == "Python" and use_case == "Create Account":
            st.markdown("### Python: Create New Account")
            
            code = '''import requests
import json

API_BASE = "https://api.cloudidp.com/v2"
API_TOKEN = "your_api_token_here"

headers = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json"
}

# Account configuration
account_data = {
    "name": "prod-app-services",
    "email": "aws+prod-app@company.com",
    "environment": "production",
    "template": "production",
    "ou_path": "Production/Applications",
    "guardrails": ["cloudtrail", "guardduty", "security_hub"],
    "budget": 5000
}

# Create account
response = requests.post(
    f"{API_BASE}/accounts",
    headers=headers,
    json=account_data
)

if response.status_code == 201:
    result = response.json()
    print(f"✅ Account created successfully!")
    print(f"Account ID: {result['id']}")
    print(f"Status: {result['status']}")
else:
    print(f"❌ Error: {response.status_code}")
    print(response.text)
'''
            
            st.code(code, language="python")
        
        elif language == "Bash/Shell":
            st.markdown("### Bash: List All Accounts")
            
            code = '''#!/bin/bash

# CloudIDP API Configuration
API_BASE="https://api.cloudidp.com/v2"
API_TOKEN="your_api_token_here"

# Get all accounts
curl -X GET "${API_BASE}/accounts" \\
  -H "Authorization: Bearer ${API_TOKEN}" \\
  -H "Content-Type: application/json" \\
  | jq '.accounts[] | {name: .name, id: .id, status: .status}'
'''
            
            st.code(code, language="bash")
    
    # ========================================================================
    # TAB 4: SDK & CLI TOOLS
    # ========================================================================
    
    @staticmethod
    def _render_sdk_cli_tools():
        """SDK and CLI tools"""
        st.subheader("🔧 SDK & CLI Tools")
        
        tool_type = st.radio("Select Tool Type", ["SDKs", "CLI Tools"], horizontal=True)
        
        if tool_type == "SDKs":
            st.markdown("### Available SDKs")
            
            # Python SDK
            with st.expander("🐍 Python SDK v2.0", expanded=True):
                st.markdown("""
                **Installation:**
                ```bash
                pip install cloudidp-sdk
                ```
                
                **Quick Example:**
                ```python
                from cloudidp import CloudIDPClient

                # Initialize client
                client = CloudIDPClient(api_token="YOUR_TOKEN")

                # List accounts
                accounts = client.accounts.list()
                for account in accounts:
                    print(f"{account.name}: {account.status}")

                # Create account
                new_account = client.accounts.create(
                    name="dev-sandbox",
                    email="aws+dev@company.com",
                    template="development"
                )
                ```
                
                **Features:**
                - ✅ Full API coverage
                - ✅ Async/await support
                - ✅ Type hints & autocomplete
                - ✅ Automatic retry logic
                - ✅ Comprehensive error handling
                
                **Documentation:** [Python SDK Docs →](#)
                """)
                
                if st.button("📥 Download Python SDK", key="dl_python"):
                    st.success("Downloading cloudidp-sdk-2.0.tar.gz...")
            
            # JavaScript SDK
            with st.expander("⚡ JavaScript/TypeScript SDK v2.0"):
                st.markdown("""
                **Installation:**
                ```bash
                npm install @cloudidp/sdk
                # or
                yarn add @cloudidp/sdk
                ```
                
                **Quick Example:**
                ```javascript
                const { CloudIDPClient } = require('@cloudidp/sdk');

                // Initialize client
                const client = new CloudIDPClient({
                  apiToken: 'YOUR_TOKEN'
                });

                // List accounts
                const accounts = await client.accounts.list();
                accounts.forEach(account => {
                  console.log(`${account.name}: ${account.status}`);
                });

                // Create account
                const newAccount = await client.accounts.create({
                  name: 'dev-sandbox',
                  email: 'aws+dev@company.com',
                  template: 'development'
                });
                ```
                
                **Documentation:** [JS SDK Docs →](#)
                """)
        
        else:  # CLI Tools
            st.markdown("### CloudIDP CLI")
            
            st.markdown("""
            Command-line interface for CloudIDP operations.
            
            **Installation:**
            ```bash
            # macOS/Linux
            curl -sSL https://cli.cloudidp.com/install.sh | bash

            # Windows (PowerShell)
            iwr -useb https://cli.cloudidp.com/install.ps1 | iex

            # Verify installation
            cloudidp --version
            ```
            """)
            
            st.markdown("---")
            st.markdown("### Common Commands")
            
            with st.expander("📋 Account Management"):
                st.code("""# List all accounts
cloudidp accounts list

# Get account details
cloudidp accounts get 123456789012

# Create account
cloudidp accounts create \\
  --name prod-app \\
  --email aws+prod@company.com \\
  --template production

# Delete account
cloudidp accounts delete 123456789012
""", language="bash")
            
            with st.expander("🔒 Security Operations"):
                st.code("""# Run security scan
cloudidp security scan --account 123456789012

# List findings
cloudidp security findings --severity CRITICAL

# Enable guardrail
cloudidp security guardrail enable \\
  --account 123456789012 \\
  --guardrail guardduty
""", language="bash")
            
            with st.expander("💰 Cost & FinOps"):
                st.code("""# Get cost report
cloudidp finops cost --last-30-days

# Detect anomalies
cloudidp finops anomalies detect

# Set budget
cloudidp finops budget set \\
  --account 123456789012 \\
  --amount 5000
""", language="bash")
    
    # ========================================================================
    # TAB 5: QUICK START
    # ========================================================================
    
    @staticmethod
    def _render_quick_start():
        """Quick start guide"""
        st.subheader("🚀 Quick Start Guide")
        
        st.markdown("""
        ### Get Started with CloudIDP in 5 Minutes!
        
        Follow these steps to start using CloudIDP programmatically.
        """)
        
        # Step-by-step guide
        st.markdown("### Step 1: Get API Token")
        st.info("""
        Navigate to **Settings → API Tokens** and create a new token.
        Copy and save it securely - you won't see it again!
        """)
        
        st.markdown("### Step 2: Install SDK")
        
        lang_choice = st.radio("Choose your language:", ["Python", "JavaScript"], horizontal=True)
        
        if lang_choice == "Python":
            st.code("pip install cloudidp-sdk", language="bash")
        else:
            st.code("npm install @cloudidp/sdk", language="bash")
        
        st.markdown("### Step 3: Initialize Client")
        
        if lang_choice == "Python":
            st.code("""from cloudidp import CloudIDPClient

# Initialize with your API token
client = CloudIDPClient(api_token="YOUR_API_TOKEN")

# Test connection
status = client.health.check()
print(f"Connection: {status}")  # Connection: OK
""", language="python")
        else:
            st.code("""const { CloudIDPClient } = require('@cloudidp/sdk');

// Initialize with your API token
const client = new CloudIDPClient({
  apiToken: 'YOUR_API_TOKEN'
});

// Test connection
const status = await client.health.check();
console.log(`Connection: ${status}`);  // Connection: OK
""", language="javascript")
        
        st.markdown("### Step 4: Your First API Call")
        
        if lang_choice == "Python":
            st.code("""# List all accounts
accounts = client.accounts.list()

print(f"Total accounts: {len(accounts)}")

for account in accounts[:5]:  # First 5
    print(f"- {account.name} ({account.id})")
""", language="python")
        else:
            st.code("""// List all accounts
const accounts = await client.accounts.list();

console.log(`Total accounts: ${accounts.length}`);

accounts.slice(0, 5).forEach(account => {
  console.log(`- ${account.name} (${account.id})`);
});
""", language="javascript")
        
        st.markdown("### Step 5: Explore More!")
        
        st.success("""
        🎉 **You're all set!**
        
        Next steps:
        - Explore [Code Samples](#) for more examples
        - Read [API Documentation](#) for full reference
        - Try the [Sandbox Environment](#) for testing
        - Use [AI Code Assistant](#) for instant help
        """)
    
    # ========================================================================
    # TAB 6: SANDBOX ENVIRONMENT
    # ========================================================================
    
    @staticmethod
    def _render_sandbox():
        """Sandbox environment for testing"""
        st.subheader("🎯 Sandbox Environment")
        
        st.markdown("""
        ### Safe Testing Environment
        
        Test your code without affecting production systems.
        """)
        
        st.info("""
        **Sandbox Features:**
        - ✅ Isolated from production
        - ✅ Rate limits: 1000 requests/hour
        - ✅ Auto-cleanup after 24 hours
        - ✅ Mock data available
        - ✅ Full API coverage
        """)
        
        st.markdown("---")
        st.markdown("### Interactive API Tester")
        
        # API endpoint selector
        col1, col2 = st.columns(2)
        
        with col1:
            method = st.selectbox("HTTP Method", ["GET", "POST", "PUT", "DELETE"])
        
        with col2:
            endpoint = st.selectbox("Endpoint", [
                "/accounts",
                "/accounts/{id}",
                "/organizations",
                "/security/findings",
                "/finops/cost"
            ])
        
        # Request body (for POST/PUT)
        if method in ["POST", "PUT"]:
            st.markdown("**Request Body:**")
            request_body = st.text_area("JSON", value='{\n  "name": "test-account"\n}', height=150)
        
        # Headers
        with st.expander("Headers (optional)"):
            st.text_input("Custom Header", placeholder="X-Custom-Header: value")
        
        # Execute
        if st.button(f"🚀 Execute {method} Request", type="primary"):
            with st.spinner("Sending request..."):
                st.success(f"✅ {method} {endpoint} - 200 OK")
                
                # Mock response
                if endpoint == "/accounts":
                    st.json({
                        "accounts": [
                            {"id": "123456789012", "name": "sandbox-account-1", "status": "active"},
                            {"id": "234567890123", "name": "sandbox-account-2", "status": "active"}
                        ],
                        "total": 2
                    })
                elif method == "POST":
                    st.json({
                        "id": "345678901234",
                        "name": "test-account",
                        "status": "created",
                        "message": "Account created in sandbox"
                    })
    
    # ========================================================================
    # TAB 7: AI CODE ASSISTANT
    # ========================================================================
    
    @staticmethod
    def _render_ai_code_assistant(ai_available: bool):
        """AI-powered code assistant"""
        st.subheader("🤖 AI Code Assistant")
        
        if not ai_available:
            st.warning("⚠️ AI Code Assistant unavailable. Configure ANTHROPIC_API_KEY to enable.")
            return
        
        st.markdown("""
        ### Get Instant Code Help from AI
        
        Ask anything about CloudIDP APIs, SDKs, or cloud development!
        """)
        
        # Quick questions
        st.markdown("#### 💡 Quick Questions:")
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("How do I create an account with Python SDK?"):
                st.code("""from cloudidp import CloudIDPClient

client = CloudIDPClient(api_token="YOUR_TOKEN")

# Create account
account = client.accounts.create(
    name="prod-services",
    email="aws+prod@company.com",
    template="production",
    guardrails=["cloudtrail", "guardduty"],
    budget=5000
)

print(f"Account created: {account.id}")
""", language="python")
            
            if st.button("How to handle API errors?"):
                st.code("""from cloudidp import CloudIDPClient, CloudIDPError

client = CloudIDPClient(api_token="YOUR_TOKEN")

try:
    account = client.accounts.get("123456789012")
except CloudIDPError as e:
    if e.status_code == 404:
        print("Account not found")
    elif e.status_code == 401:
        print("Authentication failed")
    else:
        print(f"Error: {e.message}")
""", language="python")
        
        with col2:
            if st.button("How to do batch operations?"):
                st.code("""from cloudidp import CloudIDPClient

client = CloudIDPClient(api_token="YOUR_TOKEN")

# Batch account creation
accounts_config = [
    {"name": "dev-1", "template": "development"},
    {"name": "dev-2", "template": "development"},
    {"name": "dev-3", "template": "development"}
]

results = client.accounts.batch_create(accounts_config)

for result in results:
    print(f"{result.name}: {result.status}")
""", language="python")
            
            if st.button("How to filter and search accounts?"):
                st.code("""from cloudidp import CloudIDPClient

client = CloudIDPClient(api_token="YOUR_TOKEN")

# Filter accounts
accounts = client.accounts.list(
    environment="production",
    status="active",
    tags={"Project": "WebApp"}
)

# Search by name
search_results = client.accounts.search(
    query="prod-*",
    limit=10
)
""", language="python")
        
        st.markdown("---")
        st.markdown("#### 💬 Ask AI Anything:")
        
        question = st.text_area(
            "Your Question",
            placeholder="Example: How do I implement rate limiting when calling the API?",
            height=100
        )
        
        if st.button("🤖 Get AI Answer", type="primary") and question:
            with st.spinner("AI thinking..."):
                client = get_anthropic_client()
                
                try:
                    import anthropic
                    
                    prompt = f"""You are an expert CloudIDP developer assistant. Answer this question about CloudIDP development:

Question: {question}

Provide a clear, practical answer with code examples when relevant. Use Python or JavaScript examples. Keep it concise and actionable."""

                    message = client.messages.create(
                        model="claude-sonnet-4-20250514",
                        max_tokens=2000,
                        messages=[{"role": "user", "content": prompt}]
                    )
                    
                    answer = message.content[0].text
                    
                    st.success("🤖 AI Answer:")
                    st.markdown(answer)
                
                except Exception as e:
                    st.error(f"AI Error: {str(e)}")
    
    # ========================================================================
    # TAB 8: TROUBLESHOOTING
    # ========================================================================
    
    @staticmethod
    def _render_troubleshooting(ai_available: bool):
        """Troubleshooting guide"""
        st.subheader("🐛 Troubleshooting Guide")
        
        st.markdown("### Common Issues & Solutions")
        
        # Common problems
        with st.expander("❌ 401 Unauthorized - Authentication Failed"):
            st.markdown("""
            **Cause:** Invalid or expired API token
            
            **Solutions:**
            1. Verify your API token is correct
            2. Check token hasn't expired
            3. Ensure token has required permissions
            4. Re-generate token if needed
            
            **Code Fix:**
            ```python
            # Check your token
            client = CloudIDPClient(api_token="YOUR_VALID_TOKEN")
            
            # Test authentication
            try:
                client.health.check()
                print("✅ Authentication successful")
            except CloudIDPError as e:
                print(f"❌ Auth failed: {e.message}")
            ```
            """)
        
        with st.expander("❌ 429 Too Many Requests - Rate Limited"):
            st.markdown("""
            **Cause:** Exceeded API rate limits
            
            **Solutions:**
            1. Implement exponential backoff
            2. Reduce request frequency
            3. Use batch operations where possible
            4. Consider upgrading your plan
            
            **Code Fix:**
            ```python
            import time
            from cloudidp import CloudIDPClient, RateLimitError

            client = CloudIDPClient(api_token="YOUR_TOKEN")

            def make_request_with_retry(func, max_retries=3):
                for attempt in range(max_retries):
                    try:
                        return func()
                    except RateLimitError as e:
                        if attempt < max_retries - 1:
                            wait_time = 2 ** attempt  # Exponential backoff
                            print(f"Rate limited. Waiting {wait_time}s...")
                            time.sleep(wait_time)
                        else:
                            raise

            # Use it
            accounts = make_request_with_retry(
                lambda: client.accounts.list()
            )
            ```
            """)
        
        with st.expander("❌ Connection Timeout"):
            st.markdown("""
            **Cause:** Network issues or slow response
            
            **Solutions:**
            1. Increase timeout value
            2. Check network connectivity
            3. Try again later
            4. Use async operations for long-running tasks
            
            **Code Fix:**
            ```python
            from cloudidp import CloudIDPClient

            # Increase timeout
            client = CloudIDPClient(
                api_token="YOUR_TOKEN",
                timeout=60  # 60 seconds
            )

            # Or use async
            import asyncio

            async def get_accounts():
                async with CloudIDPAsyncClient(api_token="YOUR_TOKEN") as client:
                    accounts = await client.accounts.list()
                    return accounts

            accounts = asyncio.run(get_accounts())
            ```
            """)
        
        with st.expander("❌ 422 Validation Error"):
            st.markdown("""
            **Cause:** Invalid request parameters
            
            **Solutions:**
            1. Check required fields
            2. Validate data types
            3. Review API documentation
            4. Use SDK schema validation
            
            **Code Fix:**
            ```python
            from cloudidp import CloudIDPClient
            from cloudidp.schemas import AccountCreate

            client = CloudIDPClient(api_token="YOUR_TOKEN")

            # Validate before sending
            account_data = {
                "name": "prod-app",
                "email": "aws+prod@company.com",
                "template": "production",
                "budget": 5000  # Must be integer
            }

            # SDK will validate
            try:
                account = client.accounts.create(**account_data)
            except ValidationError as e:
                print(f"Invalid data: {e.errors}")
            ```
            """)
        
        st.markdown("---")
        
        # AI-powered troubleshooting
        if ai_available:
            st.markdown("### 🤖 AI-Powered Error Analysis")
            
            error_message = st.text_area(
                "Paste your error message:",
                placeholder="""Example:
Traceback (most recent call last):
  File "test.py", line 10, in <module>
    account = client.accounts.create(name="test")
CloudIDPError: 422 Validation Error: email is required""",
                height=150
            )
            
            if st.button("🔍 Analyze Error with AI") and error_message:
                with st.spinner("AI analyzing error..."):
                    client = get_anthropic_client()
                    
                    try:
                        import anthropic
                        
                        prompt = f"""Analyze this CloudIDP API error and provide a solution:

Error:
{error_message}

Provide:
1. What caused the error
2. How to fix it
3. Code example of the fix
4. How to prevent it in the future

Be concise and practical."""

                        message = client.messages.create(
                            model="claude-sonnet-4-20250514",
                            max_tokens=1500,
                            messages=[{"role": "user", "content": prompt}]
                        )
                        
                        analysis = message.content[0].text
                        
                        st.success("🤖 AI Analysis:")
                        st.markdown(analysis)
                    
                    except Exception as e:
                        st.error(f"AI Error: {str(e)}")


# Export
__all__ = ['DevExModule']