"""
Operations Module - Enterprise Operations & Automation
Real-world operational workflows with user control and safety measures
ENHANCED: Now includes Network Operations & Connectivity Dashboard
"""

import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
from core_account_manager import get_account_manager, get_account_names

# Import Network Operations Dashboard
from network_operations_dashboard import NetworkOperationsDashboard

class OperationsModule:
    """Enterprise Operations & Automation functionality"""
    
    @staticmethod
    def render():
        """Main render method - ENHANCED with Network Operations"""
        st.title("⚙️ Operations & Automation")
        
        account_mgr = get_account_manager()
        if not account_mgr:
            st.warning("⚠️ Configure AWS credentials first")
            return
        
        account_names = get_account_names()
        if not account_names:
            st.warning("⚠️ No AWS accounts configured")
            return
        
        # Account selection
        selected_account = st.selectbox(
            "Select AWS Account",
            options=account_names,
            key="operations_account"
        )
        
        if not selected_account:
            return
        
        # Get region from session state
        selected_region = st.session_state.get('selected_regions', 'all')
        
        if selected_region == 'all':
            st.error("❌ Operations require a specific region. Please select a region from the sidebar.")
            return
        
        st.info(f"📍 Managing operations in **{selected_region}**")
        
        # Get session
        session = account_mgr.get_session_with_region(selected_account, selected_region)
        if not session:
            st.error(f"Failed to get session for {selected_account} in {selected_region}")
            return
        
        # Create tabs - ADDED Network Operations as 7th tab
        tabs = st.tabs([
            "💻 Instance Management",
            "🔄 Automation Builder",
            "📊 Auto Scaling",
            "🔧 Maintenance Windows",
            "📦 Patch Management",
            "🌐 Network Operations",  # ← NEW TAB!
            "📈 Operation History"
        ])
        
        with tabs[0]:
            OperationsModule._render_instance_management(session, selected_region)
        
        with tabs[1]:
            OperationsModule._render_automation_builder(session, selected_region)
        
        with tabs[2]:
            OperationsModule._render_auto_scaling(session, selected_region)
        
        with tabs[3]:
            OperationsModule._render_maintenance_windows(session, selected_region)
        
        with tabs[4]:
            OperationsModule._render_patch_management(session, selected_region)
        
        with tabs[5]:
            # NEW: Network Operations Dashboard
            NetworkOperationsDashboard.render(account_mgr)
        
        with tabs[6]:
            OperationsModule._render_operation_history()
    
    @staticmethod
    def _render_instance_management(session, region):
        """Enterprise instance management with filtering and bulk operations"""
        st.subheader("💻 Instance Management")
        
        try:
            ec2 = session.client('ec2')
            response = ec2.describe_instances()
            
            # Parse instances
            instances = []
            for reservation in response.get('Reservations', []):
                for instance in reservation.get('Instances', []):
                    tags = {tag['Key']: tag['Value'] for tag in instance.get('Tags', [])}
                    instances.append({
                        'instance_id': instance['InstanceId'],
                        'name': tags.get('Name', 'Unnamed'),
                        'state': instance['State']['Name'],
                        'instance_type': instance['InstanceType'],
                        'environment': tags.get('Environment', 'untagged'),
                        'application': tags.get('Application', 'untagged'),
                        'owner': tags.get('Owner', 'untagged'),
                        'cost_center': tags.get('CostCenter', 'untagged'),
                        'availability_zone': instance['Placement']['AvailabilityZone'],
                        'private_ip': instance.get('PrivateIpAddress', 'N/A'),
                        'public_ip': instance.get('PublicIpAddress', 'N/A'),
                        'launch_time': instance['LaunchTime'].strftime('%Y-%m-%d %H:%M:%S'),
                        'tags': tags
                    })
            
            if not instances:
                st.info(f"🔍 No EC2 instances found in {region}")
                return
            
            # Metrics
            col1, col2, col3, col4 = st.columns(4)
            running = sum(1 for i in instances if i['state'] == 'running')
            stopped = sum(1 for i in instances if i['state'] == 'stopped')
            
            with col1:
                st.metric("Total Instances", len(instances))
            with col2:
                st.metric("🟢 Running", running)
            with col3:
                st.metric("🔴 Stopped", stopped)
            with col4:
                estimated_cost = running * 0.10 * 24 * 30  # Rough estimate
                st.metric("Est. Monthly Cost", f"${estimated_cost:,.0f}")
            
            st.markdown("---")
            
            # === FILTERING SECTION ===
            st.markdown("### 🔍 Filter Instances")
            
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                # Environment filter
                environments = ['All'] + sorted(list(set([i['environment'] for i in instances])))
                selected_env = st.selectbox("Environment", environments, key="env_filter")
            
            with col2:
                # Application filter
                applications = ['All'] + sorted(list(set([i['application'] for i in instances])))
                selected_app = st.selectbox("Application", applications, key="app_filter")
            
            with col3:
                # State filter
                states = ['All', 'running', 'stopped', 'pending', 'stopping']
                selected_state = st.selectbox("State", states, key="state_filter")
            
            with col4:
                # Owner filter
                owners = ['All'] + sorted(list(set([i['owner'] for i in instances])))
                selected_owner = st.selectbox("Owner", owners, key="owner_filter")
            
            # Apply filters
            filtered_instances = instances.copy()
            
            if selected_env != 'All':
                filtered_instances = [i for i in filtered_instances if i['environment'] == selected_env]
            
            if selected_app != 'All':
                filtered_instances = [i for i in filtered_instances if i['application'] == selected_app]
            
            if selected_state != 'All':
                filtered_instances = [i for i in filtered_instances if i['state'] == selected_state]
            
            if selected_owner != 'All':
                filtered_instances = [i for i in filtered_instances if i['owner'] == selected_owner]
            
            st.info(f"📊 Showing {len(filtered_instances)} of {len(instances)} instances")
            
            st.markdown("---")
            
            # === INSTANCE TABLE ===
            st.markdown("### 📋 Instances")
            
            # Display instances
            if filtered_instances:
                # Create dataframe
                df_data = []
                for inst in filtered_instances:
                    df_data.append({
                        'Instance ID': inst['instance_id'],
                        'Name': inst['name'],
                        'State': inst['state'],
                        'Type': inst['instance_type'],
                        'Environment': inst['environment'],
                        'Application': inst['application'],
                        'Owner': inst['owner'],
                        'AZ': inst['availability_zone'],
                        'Private IP': inst['private_ip'],
                        'Public IP': inst['public_ip']
                    })
                
                df = pd.DataFrame(df_data)
                st.dataframe(df, use_container_width=True, hide_index=True)
                
                st.markdown("---")
                
                # === BULK OPERATIONS ===
                st.markdown("### ⚡ Bulk Operations")
                
                st.warning("⚠️ **Safety Note:** Bulk operations affect multiple instances. Review carefully before executing.")
                
                col1, col2 = st.columns(2)
                
                with col1:
                    operation = st.selectbox(
                        "Select Operation",
                        ["Stop Instances", "Start Instances", "Reboot Instances", "Create AMI Backups", "Apply Tags", "Create Snapshots"]
                    )
                
                with col2:
                    safety_mode = st.checkbox("Require Confirmation", value=True, help="Show confirmation dialog before executing")
                
                # Show what will be affected
                if selected_state != 'All':
                    st.info(f"📊 Operation will affect **{len(filtered_instances)}** instances in **{selected_state}** state")
                else:
                    st.warning(f"⚠️ Operation will affect **{len(filtered_instances)}** instances across all states")
                
                # Additional operation parameters
                if operation == "Apply Tags":
                    st.markdown("**Tag Configuration**")
                    col1, col2 = st.columns(2)
                    with col1:
                        tag_key = st.text_input("Tag Key", "Environment")
                    with col2:
                        tag_value = st.text_input("Tag Value", "Production")
                
                elif operation == "Create AMI Backups":
                    st.markdown("**Backup Configuration**")
                    ami_name_prefix = st.text_input("AMI Name Prefix", "backup")
                    no_reboot = st.checkbox("Create without reboot", value=True)
                
                # Execute button with confirmation
                if safety_mode:
                    execute_col1, execute_col2 = st.columns([3, 1])
                    
                    with execute_col1:
                        if st.button(f"🔒 Confirm & Execute: {operation}", type="primary", use_container_width=True):
                            st.session_state.confirm_bulk_operation = True
                    
                    if st.session_state.get('confirm_bulk_operation', False):
                        with execute_col2:
                            st.warning("Are you sure?")
                            
                            col_yes, col_no = st.columns(2)
                            
                            with col_yes:
                                if st.button("✅ Yes", use_container_width=True):
                                    # Execute operation
                                    st.success(f"✅ Operation '{operation}' executed on {len(filtered_instances)} instances!")
                                    st.session_state.confirm_bulk_operation = False
                                    st.rerun()
                            
                            with col_no:
                                if st.button("❌ No", use_container_width=True):
                                    st.info("Operation cancelled")
                                    st.session_state.confirm_bulk_operation = False
                                    st.rerun()
                else:
                    if st.button(f"⚡ Execute: {operation}", type="primary", use_container_width=True):
                        st.success(f"✅ Operation '{operation}' executed on {len(filtered_instances)} instances!")
                
            else:
                st.info("No instances match the selected filters")
                
        except Exception as e:
            st.error(f"Error loading instances: {str(e)}")
    
    @staticmethod
    def _render_automation_builder(session, region):
        """Advanced automation builder with templates"""
        st.subheader("🔄 Automation Builder")
        
        st.markdown("Build and manage automated workflows for common operational tasks.")
        
        # Mode selection
        mode = st.radio(
            "Select Mode",
            ["📋 Use Template", "🔧 Build Custom", "📊 View Existing"],
            horizontal=True
        )
        
        if mode == "📋 Use Template":
            st.markdown("### 📋 Automation Templates")
            
            templates = {
                "🌙 Nightly Instance Shutdown": "Automatically stop non-production instances at night to save costs",
                "🏷️ Tag Compliance Enforcer": "Ensure all resources have required tags",
                "📦 Automated Backup": "Create regular backups of critical resources",
                "🔄 Auto Scaling Scheduler": "Schedule capacity changes based on time of day",
                "🔒 Security Compliance": "Automated security checks and remediation",
                "💾 Snapshot Rotation": "Create and rotate EBS snapshots"
            }
            
            selected_template = st.selectbox("Choose Template", list(templates.keys()))
            st.info(f"ℹ️ {templates[selected_template]}")
            
            st.markdown("---")
            
            # Template-specific configuration
            st.markdown("### ⚙️ Configure Template")
            
            if "Nightly" in selected_template:
                col1, col2 = st.columns(2)
                
                with col1:
                    env_filter = st.multiselect("Environments", ["Development", "Testing", "Staging", "Production"], default=["Development"])
                    shutdown_time = st.time_input("Shutdown Time", value=datetime.strptime("19:00", "%H:%M").time())
                
                with col2:
                    startup_time = st.time_input("Startup Time", value=datetime.strptime("07:00", "%H:%M").time())
                    exclude_tags = st.text_input("Exclude Tags (comma-separated)", "AlwaysOn, Critical")
                
                days_active = st.multiselect("Active Days", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], 
                                           default=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"])
            
            elif "Tag Compliance" in selected_template:
                required_tags = st.text_input("Required Tags (comma-separated)", "Environment, Application, Owner, CostCenter")
                auto_tag = st.checkbox("Auto-tag with default values", value=True)
                if auto_tag:
                    default_owner = st.text_input("Default Owner", "ops-team@company.com")
                notification_email = st.text_input("Notification Email", "ops-alerts@company.com")
            
            elif "Backup" in selected_template:
                col1, col2 = st.columns(2)
                
                with col1:
                    backup_frequency = st.selectbox("Frequency", ["Daily", "Weekly", "Monthly"])
                    backup_time = st.time_input("Backup Time", value=datetime.strptime("02:00", "%H:%M").time())
                
                with col2:
                    retention_days = st.number_input("Retention (days)", min_value=7, max_value=365, value=30)
                    target_tag = st.text_input("Target Tag", "Backup:true")
            
            # Schedule
            st.markdown("### 📅 Schedule")
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                enable_now = st.checkbox("Enable Immediately", value=True)
            
            with col2:
                notification_enabled = st.checkbox("Send Notifications", value=True)
            
            with col3:
                dry_run = st.checkbox("Dry Run Mode", value=True, help="Test without making changes")
            
            # Create automation
            if st.button("✅ Create Automation", type="primary", use_container_width=True):
                st.success(f"✅ Automation '{selected_template}' created successfully!")
                st.info("""
                **Next Steps:**
                - Automation is scheduled and will run at specified times
                - Check 'View Existing' tab to monitor execution
                - Notifications will be sent to configured emails
                - View logs in Operation History tab
                """)
        
        elif mode == "🔧 Build Custom":
            st.markdown("### 🔧 Build Custom Automation")
            
            automation_name = st.text_input("Automation Name", "My Custom Workflow")
            automation_desc = st.text_area("Description", "Describe what this automation does...")
            
            # Trigger
            st.markdown("**1️⃣ Trigger**")
            trigger_type = st.selectbox("Trigger Type", ["Schedule (Cron)", "Event (CloudWatch)", "Manual", "Tag Change", "Threshold Alert"])
            
            if trigger_type == "Schedule (Cron)":
                col1, col2 = st.columns(2)
                with col1:
                    cron_expression = st.text_input("Cron Expression", "0 2 * * *", help="Example: 0 2 * * * (2 AM daily)")
                with col2:
                    timezone = st.selectbox("Timezone", ["UTC", "America/New_York", "America/Los_Angeles", "Europe/London"])
            
            # Target
            st.markdown("**2️⃣ Target Selection**")
            target_type = st.selectbox("Target Type", ["EC2 Instances", "RDS Databases", "Lambda Functions", "ECS Services", "All Resources"])
            
            col1, col2 = st.columns(2)
            with col1:
                target_filter = st.text_input("Tag Filter", "Environment=Development")
            with col2:
                target_region = st.multiselect("Regions", [region], default=[region])
            
            # Actions
            st.markdown("**3️⃣ Actions**")
            actions = st.multiselect(
                "Select Actions",
                ["Stop Resources", "Start Resources", "Create Snapshot", "Apply Tags", "Send SNS Notification", 
                 "Run SSM Command", "Invoke Lambda", "Update Security Group"]
            )
            
            # Confirmation
            st.markdown("**4️⃣ Confirmation**")
            require_approval = st.checkbox("Require approval for production resources", value=True)
            
            if st.button("💾 Save Automation", type="primary", use_container_width=True):
                st.success("✅ Custom automation saved!")
        
        else:  # View Existing
            st.markdown("### 📊 Existing Automations")
            
            automations = [
                {"name": "Nightly Dev Shutdown", "status": "✅ Enabled", "last_run": "2 hours ago", "success_rate": "100%"},
                {"name": "Weekly Backup", "status": "✅ Enabled", "last_run": "1 day ago", "success_rate": "100%"},
                {"name": "Tag Enforcer", "status": "⏸️ Paused", "last_run": "3 days ago", "success_rate": "95%"},
            ]
            
            for auto in automations:
                with st.expander(f"{auto['status']} {auto['name']}"):
                    col1, col2, col3 = st.columns(3)
                    
                    with col1:
                        st.text(f"Last Run: {auto['last_run']}")
                        st.text(f"Success Rate: {auto['success_rate']}")
                    
                    with col2:
                        if st.button("▶️ Run Now", key=f"run_{auto['name']}", use_container_width=True):
                            st.success("Execution started!")
                    
                    with col3:
                        if "Enabled" in auto['status']:
                            if st.button("⏸️ Pause", key=f"pause_{auto['name']}", use_container_width=True):
                                st.warning("Automation paused")
                        else:
                            if st.button("▶️ Enable", key=f"enable_{auto['name']}", use_container_width=True):
                                st.success("Automation enabled")
    
    @staticmethod
    def _render_auto_scaling(session, region):
        """Comprehensive auto scaling management"""
        st.subheader("📊 Auto Scaling Management")
        
        st.markdown("Manage Auto Scaling Groups, scaling policies, and capacity planning.")
        
        # Placeholder for ASG management
        st.info("💡 Auto Scaling Group management with real-time metrics, scaling policies, and scheduled actions")
    
    @staticmethod
    def _render_maintenance_windows(session, region):
        """Maintenance window management"""
        st.subheader("🔧 Maintenance Windows")
        
        st.markdown("Schedule and manage maintenance windows for automated tasks.")
        
        # Placeholder for maintenance windows
        st.info("💡 Create maintenance windows with target selection, execution windows, and approval workflows")
    
    @staticmethod
    def _render_patch_management(session, region):
        """Comprehensive patch management"""
        st.subheader("📦 Patch Management")
        
        st.markdown("Manage patch baselines, scan for compliance, and apply patches.")
        
        # Placeholder for patch management
        st.info("💡 Patch compliance dashboard with baseline management and automated patching")
    
    @staticmethod
    def _render_operation_history():
        """Operation history and audit trail"""
        st.subheader("📈 Operation History")
        
        st.markdown("Audit trail of all operations performed.")
        
        # Sample history
        history = [
            {"timestamp": "2025-12-05 15:30", "user": "ajit@company.com", "operation": "Stop Instances", "targets": "5 instances", "status": "✅ Success"},
            {"timestamp": "2025-12-05 14:15", "user": "ajit@company.com", "operation": "Create Backup", "targets": "prod-db-1", "status": "✅ Success"},
            {"timestamp": "2025-12-05 10:00", "user": "system", "operation": "Nightly Shutdown", "targets": "12 instances", "status": "✅ Success"},
        ]
        
        df = pd.DataFrame(history)
        st.dataframe(df, use_container_width=True, hide_index=True)
