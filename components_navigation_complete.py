"""
Main Navigation Component - FIXED for Unified Security Module
"""

import streamlit as st
from core_session_manager import SessionManager
from modules_account_management import AccountManagementModule  # AWS connection management
from modules_account_lifecycle import AccountLifecycleModule

class Navigation:
    """Main application navigation"""
    
    @staticmethod
    def render():
        """Render main navigation tabs"""
        
        # Main tabs - ALL MODULES (Security & Policy merged into one)
        tabs = st.tabs([
            "🏠 Dashboard",
            "👥 Account Management",
            "📦 Resource Inventory",
            "🌐 Network (VPC)",
            "🏢 Organizations",
            "📐 Design & Planning",
            "🚀 Provisioning",
            "🔄 CI/CD",
            "⚙️ Operations",
            "⚡ Advanced Operations",
            "🤖 Security, Compliance & AI",  # ← MERGED: Policy + Security + AI
            "🔌 EKS Management",
            "💰 FinOps & Cost",
            "🔄 Account Lifecycle",
            "👨‍💻 Developer Experience",  # ← NEW: AI-powered DevEx
            "🤖 AI Assistant"
        ])
        
        # Module 0: Dashboard
        with tabs[0]:
            try:
                from modules_dashboard import DashboardModule
                DashboardModule.render()
            except Exception as e:
                st.error(f"Error loading Dashboard: {str(e)}")
        
        # Module 1: Account Management
        with tabs[1]:
            try:
                from modules_account_management import AccountManagementModule
                AccountManagementModule.render()
            except Exception as e:
                st.error(f"Error loading Account Management: {str(e)}")
        
        # Module 2: Resource Inventory
        with tabs[2]:
            try:
                from modules_resource_inventory import ResourceInventoryModule
                ResourceInventoryModule.render()
            except Exception as e:
                st.error(f"Error loading Resource Inventory: {str(e)}")
        
        # Module 3: Network Management (VPC)
        with tabs[3]:
            try:
                from modules_network_management import NetworkManagementUI
                NetworkManagementUI.render()
            except Exception as e:
                st.error(f"Error loading Network Management: {str(e)}")
        
        # Module 4: Organizations
        with tabs[4]:
            try:
                from modules_organizations import OrganizationsManagementUI
                OrganizationsManagementUI.render()
            except Exception as e:
                st.error(f"Error loading Organizations: {str(e)}")
        
        # Module 5: Design & Planning
        with tabs[5]:
            try:
                from modules_design_planning import DesignPlanningModule
                DesignPlanningModule.render()
            except Exception as e:
                st.error(f"Error loading Design & Planning: {str(e)}")
        
        # Module 6: Provisioning & Deployment
        with tabs[6]:
            try:
                from modules_provisioning import ProvisioningModule
                ProvisioningModule.render()
            except Exception as e:
                st.error(f"Error loading Provisioning: {str(e)}")
        
        # Module 7: CI/CD (Unified - All 3 Phases)
        with tabs[7]:
            try:
                from modules_cicd_unified import UnifiedCICDModule
                UnifiedCICDModule.render()
            except Exception as e:
                st.error(f"Error loading CI/CD: {str(e)}")
        
        # Module 8: Operations
        with tabs[8]:
            try:
                from modules_operations import OperationsModule
                OperationsModule.render()
            except Exception as e:
                st.error(f"Error loading Operations: {str(e)}")
        
        # Module 9: Advanced Operations
        with tabs[9]:
            try:
                from modules_advanced_operations import AdvancedOperationsModule
                AdvancedOperationsModule.render()
            except Exception as e:
                st.error(f"Error loading Advanced Operations: {str(e)}")
        
        # Module 10: Security, Compliance & AI (UNIFIED - Policy + Security + AI)
        with tabs[10]:
            try:
                from modules_security_compliance import UnifiedSecurityComplianceModule
                UnifiedSecurityComplianceModule.render()
            except Exception as e:
                st.error(f"Error loading Security, Compliance & AI: {str(e)}")
        
        # Module 11: EKS Management
        with tabs[11]:
            try:
                from modules_eks_management import EKSManagementModule
                EKSManagementModule.render()
            except Exception as e:
                st.error(f"Error loading EKS Management: {str(e)}")
        
        # Module 12: FinOps & Cost
        with tabs[12]:
            try:
                from modules_finops import FinOpsModule
                FinOpsModule.render()
            except Exception as e:
                st.error(f"Error loading FinOps: {str(e)}")
        
        # Module 13: Account Lifecycle
        with tabs[13]:
            try:
                from modules_account_lifecycle import AccountLifecycleModule
                AccountLifecycleModule.render()
            except Exception as e:
                st.error(f"Error loading Account Lifecycle: {str(e)}")
        
        # Module 14: Developer Experience (DevEx) - AI-powered
        with tabs[14]:
            try:
                from modules_devex import DevExModule
                DevExModule.render()
            except Exception as e:
                st.error(f"Error loading Developer Experience: {str(e)}")
        
        # Module 15: AI Assistant
        with tabs[15]:
            try:
                from modules_ai_assistant import AIAssistantModule
                AIAssistantModule.render()
            except Exception as e:
                st.error(f"Error loading AI Assistant: {str(e)}")