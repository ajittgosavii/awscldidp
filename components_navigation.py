"""
Main Navigation Component - SIMPLE MULTI-ROW BUTTONS
Replaces tabs with multi-row button layout - NO SCROLLING NEEDED!
"""

import streamlit as st
from core_session_manager import SessionManager

class Navigation:
    """Main application navigation with multi-row buttons"""
    
    @staticmethod
    def render():
        """Render main navigation with buttons in multiple rows"""
        
        # Initialize active module in session state
        if 'active_module' not in st.session_state:
            st.session_state.active_module = 'Dashboard'
        
        # Define all navigation items (16 modules)
        nav_items = [
            {"key": "Dashboard", "icon": "🏠", "label": "Dashboard"},
            {"key": "Account Management", "icon": "👥", "label": "Account Mgmt"},
            {"key": "Resource Inventory", "icon": "📦", "label": "Resources"},
            {"key": "Network (VPC)", "icon": "🌐", "label": "Network"},
            {"key": "Organizations", "icon": "🏢", "label": "Organizations"},
            {"key": "Design & Planning", "icon": "📐", "label": "Design"},
            {"key": "Provisioning", "icon": "🚀", "label": "Provisioning"},
            {"key": "CI/CD", "icon": "📄", "label": "CI/CD"},
            {"key": "Operations", "icon": "⚙️", "label": "Operations"},
            {"key": "Advanced Operations", "icon": "⚡", "label": "Advanced Ops"},
            {"key": "Security", "icon": "🤖", "label": "Security & AI"},
            {"key": "EKS Management", "icon": "📌", "label": "EKS"},
            {"key": "FinOps & Cost", "icon": "💰", "label": "FinOps"},
            {"key": "Account Lifecycle", "icon": "📄", "label": "Lifecycle"},
            {"key": "Developer Experience", "icon": "👨‍💻", "label": "DevEx"},
            {"key": "AI Assistant", "icon": "🤖", "label": "AI Assistant"}
        ]
        
        # Split into 2 rows: 8 buttons each
        st.markdown("### 🧭 Navigation")
        
        # Row 1: First 8 modules
        col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)
        cols_row1 = [col1, col2, col3, col4, col5, col6, col7, col8]
        
        for idx, item in enumerate(nav_items[:8]):
            with cols_row1[idx]:
                button_type = "primary" if st.session_state.active_module == item['key'] else "secondary"
                if st.button(
                    f"{item['icon']} {item['label']}",
                    key=f"nav_{item['key']}",
                    use_container_width=True,
                    type=button_type
                ):
                    st.session_state.active_module = item['key']
                    st.rerun()
        
        # Row 2: Next 8 modules
        col9, col10, col11, col12, col13, col14, col15, col16 = st.columns(8)
        cols_row2 = [col9, col10, col11, col12, col13, col14, col15, col16]
        
        for idx, item in enumerate(nav_items[8:]):
            with cols_row2[idx]:
                button_type = "primary" if st.session_state.active_module == item['key'] else "secondary"
                if st.button(
                    f"{item['icon']} {item['label']}",
                    key=f"nav_{item['key']}",
                    use_container_width=True,
                    type=button_type
                ):
                    st.session_state.active_module = item['key']
                    st.rerun()
        
        st.markdown("---")
        
        # Render the active module
        active_module = st.session_state.active_module
        
        # Module 0: Dashboard
        if active_module == "Dashboard":
            try:
                from modules_dashboard import DashboardModule
                DashboardModule.render()
            except Exception as e:
                st.error(f"Error loading Dashboard: {str(e)}")
        
        # Module 1: Account Management
        elif active_module == "Account Management":
            try:
                from modules_account_management import AccountManagementModule
                AccountManagementModule.render()
            except Exception as e:
                st.error(f"Error loading Account Management: {str(e)}")
        
        # Module 2: Resource Inventory
        elif active_module == "Resource Inventory":
            try:
                from modules_resource_inventory import ResourceInventoryModule
                ResourceInventoryModule.render()
            except Exception as e:
                st.error(f"Error loading Resource Inventory: {str(e)}")
        
        # Module 3: Network Management (VPC)
        elif active_module == "Network (VPC)":
            try:
                from modules_network_management import NetworkManagementUI
                NetworkManagementUI.render()
            except Exception as e:
                st.error(f"Error loading Network Management: {str(e)}")
        
        # Module 4: Organizations
        elif active_module == "Organizations":
            try:
                from modules_organizations import OrganizationsManagementUI
                OrganizationsManagementUI.render()
            except Exception as e:
                st.error(f"Error loading Organizations: {str(e)}")
        
        # Module 5: Design & Planning
        elif active_module == "Design & Planning":
            try:
                from modules_design_planning import DesignPlanningModule
                DesignPlanningModule.render()
            except Exception as e:
                st.error(f"Error loading Design & Planning: {str(e)}")
        
        # Module 6: Provisioning & Deployment
        elif active_module == "Provisioning":
            try:
                from modules_provisioning import ProvisioningModule
                ProvisioningModule.render()
            except Exception as e:
                st.error(f"Error loading Provisioning: {str(e)}")
        
        # Module 7: CI/CD (Unified - All 3 Phases)
        elif active_module == "CI/CD":
            try:
                from modules_cicd_unified import UnifiedCICDModule
                UnifiedCICDModule.render()
            except Exception as e:
                st.error(f"Error loading CI/CD: {str(e)}")
        
        # Module 8: Operations
        elif active_module == "Operations":
            try:
                from modules_operations import OperationsModule
                OperationsModule.render()
            except Exception as e:
                st.error(f"Error loading Operations: {str(e)}")
        
        # Module 9: Advanced Operations
        elif active_module == "Advanced Operations":
            try:
                from modules_advanced_operations import AdvancedOperationsModule
                AdvancedOperationsModule.render()
            except Exception as e:
                st.error(f"Error loading Advanced Operations: {str(e)}")
        
        # Module 10: Security, Compliance & AI
        elif active_module == "Security":
            try:
                from modules_security_compliance import UnifiedSecurityComplianceModule
                UnifiedSecurityComplianceModule.render()
            except Exception as e:
                st.error(f"Error loading Security, Compliance & AI: {str(e)}")
        
        # Module 11: EKS Management
        elif active_module == "EKS Management":
            try:
                from modules_eks_management import EKSManagementModule
                EKSManagementModule.render()
            except Exception as e:
                st.error(f"Error loading EKS Management: {str(e)}")
        
        # Module 12: FinOps & Cost
        elif active_module == "FinOps & Cost":
            try:
                from modules_finops import FinOpsModule
                FinOpsModule.render()
            except Exception as e:
                st.error(f"Error loading FinOps: {str(e)}")
        
        # Module 13: Account Lifecycle
        elif active_module == "Account Lifecycle":
            try:
                from modules_account_lifecycle import AccountLifecycleModule
                AccountLifecycleModule.render()
            except Exception as e:
                st.error(f"Error loading Account Lifecycle: {str(e)}")
        
        # Module 14: Developer Experience
        elif active_module == "Developer Experience":
            try:
                from modules_devex import DevExModule
                DevExModule.render()
            except Exception as e:
                st.error(f"Error loading Developer Experience: {str(e)}")
        
        # Module 15: AI Assistant
        elif active_module == "AI Assistant":
            try:
                from modules_ai_assistant import AIAssistantModule
                AIAssistantModule.render()
            except Exception as e:
                st.error(f"Error loading AI Assistant: {str(e)}")
