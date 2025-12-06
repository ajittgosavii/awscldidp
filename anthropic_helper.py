"""
Anthropic AI Integration - Claude API Helper
Provides AI-powered features for CloudIDP Enhanced
"""

import os
import streamlit as st
from typing import Optional, Dict, List
import json

try:
    import anthropic
    ANTHROPIC_AVAILABLE = True
except ImportError:
    ANTHROPIC_AVAILABLE = False

class AnthropicHelper:
    """Helper class for Anthropic Claude API integration"""
    
    def __init__(self):
        """Initialize Anthropic client"""
        self.client = None
        self.api_key = None
        
        # Check for API key in multiple locations
        if ANTHROPIC_AVAILABLE:
            self.api_key = self._get_api_key()
            if self.api_key:
                try:
                    self.client = anthropic.Anthropic(api_key=self.api_key)
                except Exception as e:
                    st.warning(f"⚠️ Failed to initialize Anthropic client: {e}")
    
    def _get_api_key(self) -> Optional[str]:
        """Get API key from various sources"""
        # Try secrets first
        try:
            if "anthropic" in st.secrets:
                return st.secrets["anthropic"].get("api_key")
        except:
            pass
        
        # Try environment variable
        api_key = os.environ.get("ANTHROPIC_API_KEY")
        if api_key:
            return api_key
        
        # Try session state
        if "anthropic_api_key" in st.session_state:
            return st.session_state.anthropic_api_key
        
        return None
    
    def is_available(self) -> bool:
        """Check if Anthropic integration is available"""
        return ANTHROPIC_AVAILABLE and self.client is not None
    
    def generate_architecture_recommendation(
        self, 
        requirements: Dict[str, any]
    ) -> Optional[str]:
        """Generate architecture recommendations using Claude"""
        if not self.is_available():
            return None
        
        try:
            prompt = f"""Based on these AWS requirements, provide architecture recommendations:
            
Requirements:
- Services needed: {requirements.get('services', [])}
- Expected traffic: {requirements.get('traffic', 'unknown')}
- Compliance requirements: {requirements.get('compliance', [])}
- Budget: {requirements.get('budget', 'unknown')}
- High availability: {requirements.get('ha_required', False)}

Provide a clear, structured architecture recommendation including:
1. Recommended AWS services
2. Architecture diagram description
3. Estimated costs
4. Security considerations
5. Scaling strategy
"""
            
            message = self.client.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=2000,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            
            return message.content[0].text
            
        except Exception as e:
            st.error(f"Error generating recommendation: {e}")
            return None
    
    def analyze_cost_optimization(
        self, 
        resources: List[Dict]
    ) -> Optional[str]:
        """Analyze resources and provide cost optimization recommendations"""
        if not self.is_available():
            return None
        
        try:
            prompt = f"""Analyze these AWS resources and provide cost optimization recommendations:

Resources:
{json.dumps(resources, indent=2, default=str)}

Provide:
1. Identified cost optimization opportunities
2. Potential savings estimates
3. Implementation steps
4. Risk assessment
"""
            
            message = self.client.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=2000,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            
            return message.content[0].text
            
        except Exception as e:
            st.error(f"Error analyzing costs: {e}")
            return None
    
    def generate_iac_template(
        self, 
        infrastructure: Dict[str, any],
        format: str = "terraform"
    ) -> Optional[str]:
        """Generate Infrastructure as Code template"""
        if not self.is_available():
            return None
        
        try:
            prompt = f"""Generate a {format.upper()} template for this infrastructure:

Infrastructure:
{json.dumps(infrastructure, indent=2, default=str)}

Provide:
1. Complete {format} code
2. Variables definition
3. Outputs
4. Best practices applied
"""
            
            message = self.client.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=3000,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            
            return message.content[0].text
            
        except Exception as e:
            st.error(f"Error generating IaC: {e}")
            return None
    
    def analyze_security_findings(
        self, 
        findings: List[Dict]
    ) -> Optional[str]:
        """Analyze security findings and provide recommendations"""
        if not self.is_available():
            return None
        
        try:
            prompt = f"""Analyze these AWS security findings and provide recommendations:

Security Findings:
{json.dumps(findings, indent=2, default=str)}

Provide:
1. Severity assessment
2. Remediation steps (prioritized)
3. Prevention strategies
4. Compliance impact
"""
            
            message = self.client.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=2000,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            
            return message.content[0].text
            
        except Exception as e:
            st.error(f"Error analyzing security: {e}")
            return None
    
    def generate_runbook(
        self, 
        operation: str,
        context: Dict[str, any]
    ) -> Optional[str]:
        """Generate operational runbook"""
        if not self.is_available():
            return None
        
        try:
            prompt = f"""Generate a detailed operational runbook for: {operation}

Context:
{json.dumps(context, indent=2, default=str)}

Include:
1. Prerequisites
2. Step-by-step procedure
3. Rollback steps
4. Verification steps
5. Troubleshooting guide
"""
            
            message = self.client.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=2500,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            
            return message.content[0].text
            
        except Exception as e:
            st.error(f"Error generating runbook: {e}")
            return None
    
    def chat(self, user_message: str, conversation_history: List[Dict] = None) -> Optional[str]:
        """General chat interface with Claude"""
        if not self.is_available():
            return None
        
        try:
            messages = conversation_history or []
            messages.append({"role": "user", "content": user_message})
            
            message = self.client.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=1500,
                messages=messages
            )
            
            return message.content[0].text
            
        except Exception as e:
            st.error(f"Error in chat: {e}")
            return None

# Global instance
@st.cache_resource
def get_anthropic_helper() -> AnthropicHelper:
    """Get cached Anthropic helper instance"""
    return AnthropicHelper()
