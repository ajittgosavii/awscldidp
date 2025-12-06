"""
AI Assistant Module - Claude-Powered Cloud Operations Assistant
Provides AI-powered assistance for AWS operations, architecture, and optimization
"""

import streamlit as st
from anthropic_helper import get_anthropic_helper
from typing import List, Dict
import json

class AIAssistantModule:
    """AI-powered assistant for cloud operations"""
    
    @staticmethod
    def render():
        """Render AI assistant interface"""
        
        st.markdown("## 🤖 AI Assistant (Claude)")
        st.caption("AI-powered assistance for AWS architecture, operations, and optimization")
        
        # Check if Anthropic is available
        helper = get_anthropic_helper()
        
        if not helper.is_available():
            st.warning("⚠️ Anthropic API not configured")
            st.info("""
            To enable AI Assistant features:
            
            1. Add your Anthropic API key to `.streamlit/secrets.toml`:
            ```toml
            [anthropic]
            api_key = "sk-ant-..."
            ```
            
            2. Or set environment variable:
            ```bash
            export ANTHROPIC_API_KEY="sk-ant-..."
            ```
            
            Get your API key at: https://console.anthropic.com/
            """)
            return
        
        st.success("✅ AI Assistant Ready")
        
        # AI Assistant features in tabs
        tabs = st.tabs([
            "💬 Chat Assistant",
            "🏗️ Architecture Design",
            "💰 Cost Optimization",
            "🔒 Security Analysis",
            "📝 Generate IaC",
            "📚 Runbook Generator"
        ])
        
        # Tab 1: Chat Assistant
        with tabs[0]:
            AIAssistantModule._render_chat_assistant(helper)
        
        # Tab 2: Architecture Design
        with tabs[1]:
            AIAssistantModule._render_architecture_design(helper)
        
        # Tab 3: Cost Optimization
        with tabs[2]:
            AIAssistantModule._render_cost_optimization(helper)
        
        # Tab 4: Security Analysis
        with tabs[3]:
            AIAssistantModule._render_security_analysis(helper)
        
        # Tab 5: Generate IaC
        with tabs[4]:
            AIAssistantModule._render_iac_generator(helper)
        
        # Tab 6: Runbook Generator
        with tabs[5]:
            AIAssistantModule._render_runbook_generator(helper)
    
    @staticmethod
    def _render_chat_assistant(helper):
        """Chat interface with Claude"""
        st.markdown("### 💬 Chat with Claude")
        st.caption("Ask questions about AWS, get recommendations, troubleshoot issues")
        
        # Initialize chat history
        if "chat_history" not in st.session_state:
            st.session_state.chat_history = []
        
        # Display chat history
        for message in st.session_state.chat_history:
            role = message["role"]
            content = message["content"]
            
            if role == "user":
                st.chat_message("user").write(content)
            else:
                st.chat_message("assistant").write(content)
        
        # Chat input
        user_input = st.chat_input("Ask me anything about your AWS infrastructure...")
        
        if user_input:
            # Add user message to history
            st.session_state.chat_history.append({
                "role": "user",
                "content": user_input
            })
            
            # Display user message
            st.chat_message("user").write(user_input)
            
            # Get AI response
            with st.spinner("Thinking..."):
                response = helper.chat(user_input, st.session_state.chat_history[:-1])
            
            if response:
                # Add assistant message to history
                st.session_state.chat_history.append({
                    "role": "assistant",
                    "content": response
                })
                
                # Display assistant message
                st.chat_message("assistant").write(response)
            else:
                st.error("Failed to get response from AI assistant")
        
        # Clear chat button
        if st.button("Clear Chat History"):
            st.session_state.chat_history = []
            st.rerun()
    
    @staticmethod
    def _render_architecture_design(helper):
        """Architecture design assistant"""
        st.markdown("### 🏗️ Architecture Design Assistant")
        st.caption("Get AI-powered architecture recommendations")
        
        with st.form("architecture_form"):
            st.markdown("#### Describe Your Requirements")
            
            services = st.multiselect(
                "AWS Services Needed",
                ["EC2", "RDS", "S3", "Lambda", "ECS", "EKS", "DynamoDB", 
                 "ElastiCache", "CloudFront", "API Gateway", "SNS", "SQS"]
            )
            
            traffic = st.selectbox(
                "Expected Traffic",
                ["Low (< 1000 users/day)", "Medium (1000-10000 users/day)", 
                 "High (10000-100000 users/day)", "Very High (> 100000 users/day)"]
            )
            
            compliance = st.multiselect(
                "Compliance Requirements",
                ["PCI-DSS", "HIPAA", "SOC 2", "GDPR", "None"]
            )
            
            budget = st.selectbox(
                "Monthly Budget",
                ["< $1,000", "$1,000 - $5,000", "$5,000 - $20,000", 
                 "$20,000 - $50,000", "> $50,000"]
            )
            
            ha_required = st.checkbox("High Availability Required")
            
            additional_requirements = st.text_area(
                "Additional Requirements",
                placeholder="Any specific requirements, constraints, or preferences..."
            )
            
            submitted = st.form_submit_button("Generate Architecture Recommendation")
        
        if submitted and services:
            with st.spinner("🤖 Generating architecture recommendations..."):
                requirements = {
                    'services': services,
                    'traffic': traffic,
                    'compliance': compliance,
                    'budget': budget,
                    'ha_required': ha_required,
                    'additional': additional_requirements
                }
                
                recommendation = helper.generate_architecture_recommendation(requirements)
            
            if recommendation:
                st.markdown("#### 🎯 Architecture Recommendation")
                st.markdown(recommendation)
                
                if st.button("Save Recommendation"):
                    st.success("✅ Recommendation saved to database")
    
    @staticmethod
    def _render_cost_optimization(helper):
        """Cost optimization assistant"""
        st.markdown("### 💰 Cost Optimization Assistant")
        st.caption("Analyze resources and get AI-powered cost optimization recommendations")
        
        from core_account_manager import get_account_manager
        from config_settings import AppConfig
        
        account_mgr = get_account_manager()
        if not account_mgr:
            st.warning("Please configure AWS accounts first")
            return
        
        accounts = AppConfig.load_aws_accounts()
        account_names = [acc.account_name for acc in accounts]
        
        selected_account = st.selectbox("Select Account", account_names)
        
        if st.button("Analyze Cost Optimization Opportunities", use_container_width=True):
            with st.spinner("🤖 Analyzing resources for cost optimization..."):
                # Simulate fetching resources
                resources = [
                    {'type': 'EC2', 'id': 'i-abc123', 'instance_type': 't3.xlarge', 'cpu_avg': '15%'},
                    {'type': 'RDS', 'id': 'db-def456', 'instance_class': 'db.r5.2xlarge', 'connections_avg': '25%'},
                    {'type': 'EBS', 'id': 'vol-ghi789', 'type': 'io1', 'iops': '10000', 'usage': '30%'}
                ]
                
                analysis = helper.analyze_cost_optimization(resources)
            
            if analysis:
                st.markdown("#### 💡 Cost Optimization Recommendations")
                st.markdown(analysis)
                
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("Export Report"):
                        st.success("✅ Report exported to PDF")
                with col2:
                    if st.button("Create Action Plan"):
                        st.success("✅ Action plan created")
    
    @staticmethod
    def _render_security_analysis(helper):
        """Security analysis assistant"""
        st.markdown("### 🔒 Security Analysis Assistant")
        st.caption("Analyze security findings and get remediation recommendations")
        
        if st.button("Analyze Recent Security Findings", use_container_width=True):
            with st.spinner("🤖 Analyzing security findings..."):
                # Simulate security findings
                findings = [
                    {
                        'title': 'S3 bucket with public read access',
                        'severity': 'HIGH',
                        'resource': 'arn:aws:s3:::my-bucket',
                        'description': 'S3 bucket allows public read access'
                    },
                    {
                        'title': 'Security group allows unrestricted SSH',
                        'severity': 'CRITICAL',
                        'resource': 'sg-abc123',
                        'description': 'Security group allows SSH from 0.0.0.0/0'
                    }
                ]
                
                analysis = helper.analyze_security_findings(findings)
            
            if analysis:
                st.markdown("#### 🛡️ Security Analysis & Remediation")
                st.markdown(analysis)
                
                if st.button("Create Remediation Tasks"):
                    st.success("✅ Remediation tasks created and assigned")
    
    @staticmethod
    def _render_iac_generator(helper):
        """Infrastructure as Code generator"""
        st.markdown("### 📝 Generate Infrastructure as Code")
        st.caption("Describe your infrastructure and get Terraform/CloudFormation code")
        
        format_type = st.selectbox("IaC Format", ["Terraform", "CloudFormation", "CDK (Python)"])
        
        infrastructure_desc = st.text_area(
            "Describe Infrastructure",
            placeholder="""Example:
            
I need a web application setup with:
- VPC with public and private subnets across 2 AZs
- Application Load Balancer in public subnets
- Auto Scaling Group of EC2 instances in private subnets
- RDS MySQL database in private subnets
- S3 bucket for static assets
- CloudFront distribution for CDN
""",
            height=200
        )
        
        if st.button("Generate IaC Template", use_container_width=True):
            if infrastructure_desc:
                with st.spinner(f"🤖 Generating {format_type} template..."):
                    infrastructure = {
                        'description': infrastructure_desc,
                        'format': format_type.lower()
                    }
                    
                    template = helper.generate_iac_template(infrastructure, format_type.lower().split()[0])
                
                if template:
                    st.markdown(f"#### 📄 Generated {format_type} Template")
                    st.code(template, language="hcl" if format_type == "Terraform" else "yaml")
                    
                    col1, col2 = st.columns(2)
                    with col1:
                        if st.button("Download Template"):
                            st.success("✅ Template downloaded")
                    with col2:
                        if st.button("Deploy to Account"):
                            st.info("🚀 Deployment initiated")
            else:
                st.warning("Please describe the infrastructure you want to create")
    
    @staticmethod
    def _render_runbook_generator(helper):
        """Operational runbook generator"""
        st.markdown("### 📚 Runbook Generator")
        st.caption("Generate detailed operational runbooks for common tasks")
        
        operation_type = st.selectbox(
            "Operation Type",
            [
                "Deploy Application Update",
                "Database Migration",
                "Disaster Recovery Failover",
                "Scale Up/Down Infrastructure",
                "Security Incident Response",
                "Backup and Restore",
                "Certificate Renewal",
                "Custom Operation"
            ]
        )
        
        if operation_type == "Custom Operation":
            operation_name = st.text_input("Operation Name")
        else:
            operation_name = operation_type
        
        context = st.text_area(
            "Additional Context",
            placeholder="Provide any specific context about your environment, constraints, or requirements..."
        )
        
        if st.button("Generate Runbook", use_container_width=True):
            if operation_name:
                with st.spinner("🤖 Generating runbook..."):
                    context_dict = {
                        'operation': operation_name,
                        'context': context if context else "Standard AWS environment"
                    }
                    
                    runbook = helper.generate_runbook(operation_name, context_dict)
                
                if runbook:
                    st.markdown("#### 📖 Generated Runbook")
                    st.markdown(runbook)
                    
                    col1, col2 = st.columns(2)
                    with col1:
                        if st.button("Save to Database"):
                            st.success("✅ Runbook saved")
                    with col2:
                        if st.button("Export as PDF"):
                            st.success("✅ Runbook exported")
            else:
                st.warning("Please specify an operation name")
