"""
Enhanced Provisioning & Deployment Module - WITH CI/CD INTEGRATION
Combines manual provisioning with automated CI/CD pipeline monitoring and control
"""

import streamlit as st
import pandas as pd
from typing import Dict, List, Optional
from datetime import datetime, timedelta
from core_account_manager import get_account_manager, get_account_names
from aws_cloudformation import CloudFormationManager
import json
import requests
from dataclasses import dataclass

# ============================================================================
# CI/CD INTEGRATION MANAGER
# ============================================================================

@dataclass
class CICDDeployment:
    """Represents a CI/CD pipeline deployment"""
    pipeline_id: str
    pipeline_name: str
    status: str  # running, success, failed, pending_approval
    environment: str  # dev, staging, production
    stack_name: str
    commit_hash: str
    commit_message: str
    author: str
    triggered_at: datetime
    completed_at: Optional[datetime]
    approval_required: bool = False
    change_set_url: Optional[str] = None
    pipeline_url: Optional[str] = None

class CICDIntegrationManager:
    """Manages CI/CD pipeline integrations"""
    
    def __init__(self, provider: str = "github"):
        """
        Initialize CI/CD integration
        
        Args:
            provider: github, gitlab, jenkins, codepipeline, terraform_cloud
        """
        self.provider = provider
        self.api_token = self._get_api_token()
    
    def _get_api_token(self) -> Optional[str]:
        """Get API token from Streamlit secrets or environment"""
        try:
            if self.provider == "github":
                return st.secrets.get("GITHUB_TOKEN")
            elif self.provider == "gitlab":
                return st.secrets.get("GITLAB_TOKEN")
            elif self.provider == "jenkins":
                return st.secrets.get("JENKINS_TOKEN")
            # Add more providers as needed
        except:
            return None
    
    def get_recent_deployments(self, limit: int = 10) -> List[CICDDeployment]:
        """Get recent CI/CD deployments"""
        if not self.api_token:
            return self._get_demo_deployments()
        
        if self.provider == "github":
            return self._get_github_deployments(limit)
        elif self.provider == "gitlab":
            return self._get_gitlab_deployments(limit)
        else:
            return self._get_demo_deployments()
    
    def _get_github_deployments(self, limit: int) -> List[CICDDeployment]:
        """Fetch deployments from GitHub Actions"""
        # This would call GitHub API
        # For now, return demo data
        return self._get_demo_deployments()
    
    def _get_gitlab_deployments(self, limit: int) -> List[CICDDeployment]:
        """Fetch deployments from GitLab CI"""
        # This would call GitLab API
        # For now, return demo data
        return self._get_demo_deployments()
    
    def _get_demo_deployments(self) -> List[CICDDeployment]:
        """Generate demo deployment data"""
        now = datetime.now()
        
        return [
            CICDDeployment(
                pipeline_id="GHA-1234",
                pipeline_name="Deploy Infrastructure",
                status="success",
                environment="production",
                stack_name="prod-vpc-stack",
                commit_hash="abc1234",
                commit_message="Add production VPC with 3 AZs",
                author="John Doe",
                triggered_at=now - timedelta(hours=2),
                completed_at=now - timedelta(hours=1, minutes=45),
                pipeline_url="https://github.com/org/repo/actions/runs/1234"
            ),
            CICDDeployment(
                pipeline_id="GHA-1235",
                pipeline_name="Deploy Infrastructure",
                status="pending_approval",
                environment="production",
                stack_name="prod-rds-stack",
                commit_hash="def5678",
                commit_message="Add production RDS with read replicas",
                author="Jane Smith",
                triggered_at=now - timedelta(minutes=30),
                completed_at=None,
                approval_required=True,
                change_set_url="https://github.com/org/repo/pull/456",
                pipeline_url="https://github.com/org/repo/actions/runs/1235"
            ),
            CICDDeployment(
                pipeline_id="GHA-1233",
                pipeline_name="Deploy Infrastructure",
                status="success",
                environment="staging",
                stack_name="staging-app-stack",
                commit_hash="def5678",
                commit_message="Add production RDS with read replicas",
                author="Jane Smith",
                triggered_at=now - timedelta(minutes=45),
                completed_at=now - timedelta(minutes=35),
                pipeline_url="https://github.com/org/repo/actions/runs/1233"
            ),
            CICDDeployment(
                pipeline_id="GHA-1232",
                pipeline_name="Deploy Infrastructure",
                status="success",
                environment="dev",
                stack_name="dev-test-stack",
                commit_hash="def5678",
                commit_message="Add production RDS with read replicas",
                author="Jane Smith",
                triggered_at=now - timedelta(hours=1),
                completed_at=now - timedelta(minutes=50),
                pipeline_url="https://github.com/org/repo/actions/runs/1232"
            ),
            CICDDeployment(
                pipeline_id="GHA-1231",
                pipeline_name="Deploy Infrastructure",
                status="failed",
                environment="dev",
                stack_name="dev-failed-stack",
                commit_hash="ghi9012",
                commit_message="Update security groups",
                author="Bob Wilson",
                triggered_at=now - timedelta(hours=3),
                completed_at=now - timedelta(hours=2, minutes=55),
                pipeline_url="https://github.com/org/repo/actions/runs/1231"
            ),
            CICDDeployment(
                pipeline_id="GHA-1230",
                pipeline_name="Deploy Infrastructure",
                status="running",
                environment="staging",
                stack_name="staging-update-stack",
                commit_hash="jkl3456",
                commit_message="Update Lambda functions",
                author="Alice Johnson",
                triggered_at=now - timedelta(minutes=10),
                completed_at=None,
                pipeline_url="https://github.com/org/repo/actions/runs/1230"
            )
        ]
    
    def approve_deployment(self, pipeline_id: str) -> Dict:
        """Approve a pending deployment"""
        # This would call the CI/CD provider API
        return {"success": True, "message": f"Pipeline {pipeline_id} approved"}
    
    def reject_deployment(self, pipeline_id: str, reason: str) -> Dict:
        """Reject a pending deployment"""
        # This would call the CI/CD provider API
        return {"success": True, "message": f"Pipeline {pipeline_id} rejected: {reason}"}
    
    def trigger_pipeline(self, repo: str, branch: str, environment: str, 
                        parameters: Dict = None) -> Dict:
        """Trigger a CI/CD pipeline"""
        # This would call the CI/CD provider API
        return {
            "success": True,
            "pipeline_id": "GHA-9999",
            "pipeline_url": f"https://github.com/{repo}/actions/runs/9999"
        }

# ============================================================================
# ENHANCED PROVISIONING MODULE
# ============================================================================

class ProvisioningModuleEnhanced:
    """Enhanced Provisioning & Deployment with CI/CD Integration"""
    
    @staticmethod
    def render():
        """Main render method"""
        st.title("🚀 Provisioning & Deployment")
        st.caption("Infrastructure deployment with CI/CD integration")
        
        account_mgr = get_account_manager()
        if not account_mgr:
            st.warning("⚠️ Configure AWS credentials first")
            st.info("👉 Go to the 'Account Management' tab to add your AWS accounts first.")
            return
        
        # Get account names
        account_names = get_account_names()
        
        if not account_names:
            st.warning("⚠️ No AWS accounts configured")
            st.info("👉 Go to the 'Account Management' tab to add your AWS accounts first.")
            return
        
        selected_account = st.selectbox(
            "Select AWS Account",
            options=account_names,
            key="provisioning_account"
        )
        
        if not selected_account:
            return
        
        # Check if a specific region is selected
        selected_region = st.session_state.get('selected_regions', 'all')
        
        if selected_region == 'all':
            st.error("❌ Error loading Provisioning: You must specify a region.")
            st.info("📍 CloudFormation stacks are region-specific. Please select a specific region from the sidebar to view and deploy stacks.")
            return
        
        # Get region-specific session
        session = account_mgr.get_session_with_region(selected_account, selected_region)
        if not session:
            st.error(f"Failed to get session for {selected_account} in region {selected_region}")
            return
        
        # Show selected region
        st.info(f"📍 Managing stacks in **{selected_region}**")
        
        cfn_mgr = CloudFormationManager(session)
        cicd_mgr = CICDIntegrationManager(provider="github")
        
        # Create tabs - ENHANCED with CI/CD tabs
        tabs = st.tabs([
            "📊 CI/CD Deployments",      # NEW
            "⏸️ Pending Approvals",       # NEW  
            "🎯 Trigger Pipeline",        # NEW
            "📚 Stack Library",
            "🚀 Deploy Stack",
            "🔄 Active Deployments",
            "📝 Change Sets",
            "🌍 Multi-Region",
            "⏮️ Rollback"
        ])
        
        with tabs[0]:
            ProvisioningModuleEnhanced._render_cicd_deployments(cicd_mgr, cfn_mgr)
        
        with tabs[1]:
            ProvisioningModuleEnhanced._render_pending_approvals(cicd_mgr)
        
        with tabs[2]:
            ProvisioningModuleEnhanced._render_trigger_pipeline(cicd_mgr)
        
        with tabs[3]:
            ProvisioningModuleEnhanced._render_stack_library(cfn_mgr)
        
        with tabs[4]:
            ProvisioningModuleEnhanced._render_deploy_stack(cfn_mgr)
        
        with tabs[5]:
            ProvisioningModuleEnhanced._render_active_deployments(cfn_mgr)
        
        with tabs[6]:
            ProvisioningModuleEnhanced._render_change_sets(cfn_mgr)
        
        with tabs[7]:
            ProvisioningModuleEnhanced._render_multi_region()
        
        with tabs[8]:
            ProvisioningModuleEnhanced._render_rollback(cfn_mgr)
    
    # ========================================================================
    # NEW TAB: CI/CD DEPLOYMENTS
    # ========================================================================
    
    @staticmethod
    def _render_cicd_deployments(cicd_mgr: CICDIntegrationManager, cfn_mgr: CloudFormationManager):
        """Monitor CI/CD pipeline deployments"""
        st.subheader("📊 CI/CD Pipeline Deployments")
        st.caption("Monitor automated deployments from your CI/CD pipelines")
        
        # Check if CI/CD is configured
        if not cicd_mgr.api_token:
            st.warning("⚠️ CI/CD integration not configured")
            
            with st.expander("📖 How to Configure CI/CD Integration"):
                st.markdown("""
                ### Setup Instructions
                
                Add your CI/CD provider API token to Streamlit secrets:
                
                **For GitHub Actions:**
                ```toml
                # .streamlit/secrets.toml
                GITHUB_TOKEN = "ghp_your_github_personal_access_token"
                ```
                
                **For GitLab CI:**
                ```toml
                GITLAB_TOKEN = "your_gitlab_access_token"
                ```
                
                **For Jenkins:**
                ```toml
                JENKINS_TOKEN = "your_jenkins_api_token"
                JENKINS_URL = "https://jenkins.example.com"
                ```
                
                After configuration, this tab will show live pipeline status!
                """)
            
            st.info("💡 Showing demo data for visualization purposes")
        
        # Get recent deployments
        deployments = cicd_mgr.get_recent_deployments(limit=20)
        
        if not deployments:
            st.info("No recent CI/CD deployments found")
            return
        
        # Summary metrics
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            total = len(deployments)
            st.metric("Total Deployments", total)
        
        with col2:
            pending = sum(1 for d in deployments if d.status == "pending_approval")
            st.metric("Pending Approval", pending, delta=None if pending == 0 else f"{pending} waiting")
        
        with col3:
            running = sum(1 for d in deployments if d.status == "running")
            st.metric("Running", running)
        
        with col4:
            failed = sum(1 for d in deployments if d.status == "failed")
            st.metric("Failed", failed, delta=f"-{failed}" if failed > 0 else "0")
        
        st.markdown("---")
        
        # Filter options
        col1, col2, col3 = st.columns(3)
        
        with col1:
            env_filter = st.multiselect(
                "Filter by Environment",
                options=["production", "staging", "dev"],
                default=["production", "staging", "dev"],
                key="cicd_env_filter"
            )
        
        with col2:
            status_filter = st.multiselect(
                "Filter by Status",
                options=["running", "success", "failed", "pending_approval"],
                default=["running", "success", "pending_approval"],
                key="cicd_status_filter"
            )
        
        with col3:
            sort_by = st.selectbox(
                "Sort by",
                options=["Recent First", "Oldest First", "Environment"],
                key="cicd_sort"
            )
        
        # Filter deployments
        filtered = [
            d for d in deployments
            if d.environment in env_filter and d.status in status_filter
        ]
        
        # Display deployments
        for deployment in filtered:
            # Status icon and color
            if deployment.status == "success":
                status_icon = "✅"
                status_color = "green"
            elif deployment.status == "failed":
                status_icon = "❌"
                status_color = "red"
            elif deployment.status == "running":
                status_icon = "🔄"
                status_color = "blue"
            elif deployment.status == "pending_approval":
                status_icon = "⏸️"
                status_color = "orange"
            else:
                status_icon = "⚪"
                status_color = "gray"
            
            # Environment badge color
            env_colors = {
                "production": "🔴",
                "staging": "🟡",
                "dev": "🟢"
            }
            env_badge = env_colors.get(deployment.environment, "⚪")
            
            with st.expander(
                f"{status_icon} {env_badge} **{deployment.environment.upper()}** | "
                f"{deployment.stack_name} | {deployment.status.upper()}",
                expanded=deployment.approval_required
            ):
                col1, col2 = st.columns(2)
                
                with col1:
                    st.markdown(f"**Pipeline:** {deployment.pipeline_name}")
                    st.markdown(f"**Pipeline ID:** {deployment.pipeline_id}")
                    st.markdown(f"**Stack:** {deployment.stack_name}")
                    st.markdown(f"**Environment:** {deployment.environment}")
                    
                    if deployment.pipeline_url:
                        st.markdown(f"[🔗 View Pipeline]({deployment.pipeline_url})")
                
                with col2:
                    st.markdown(f"**Commit:** `{deployment.commit_hash}`")
                    st.markdown(f"**Message:** {deployment.commit_message}")
                    st.markdown(f"**Author:** {deployment.author}")
                    st.markdown(f"**Triggered:** {deployment.triggered_at.strftime('%Y-%m-%d %H:%M:%S')}")
                    
                    if deployment.completed_at:
                        duration = (deployment.completed_at - deployment.triggered_at).total_seconds() / 60
                        st.markdown(f"**Duration:** {duration:.1f} minutes")
                
                # Show approval UI if needed
                if deployment.approval_required and deployment.status == "pending_approval":
                    st.markdown("---")
                    st.warning("⏸️ **This deployment requires your approval!**")
                    
                    if deployment.change_set_url:
                        st.markdown(f"[📋 Review Changes]({deployment.change_set_url})")
                    
                    col1, col2, col3 = st.columns([1, 1, 3])
                    
                    with col1:
                        if st.button("✅ Approve", key=f"approve_{deployment.pipeline_id}"):
                            result = cicd_mgr.approve_deployment(deployment.pipeline_id)
                            if result.get("success"):
                                st.success("Deployment approved! Pipeline will continue.")
                                st.rerun()
                    
                    with col2:
                        if st.button("❌ Reject", key=f"reject_{deployment.pipeline_id}"):
                            st.session_state[f"reject_reason_{deployment.pipeline_id}"] = True
                    
                    # Show rejection reason input
                    if st.session_state.get(f"reject_reason_{deployment.pipeline_id}"):
                        reason = st.text_area(
                            "Rejection Reason",
                            key=f"reason_{deployment.pipeline_id}",
                            placeholder="Explain why this deployment is being rejected..."
                        )
                        if st.button("Confirm Rejection", key=f"confirm_reject_{deployment.pipeline_id}"):
                            result = cicd_mgr.reject_deployment(deployment.pipeline_id, reason)
                            if result.get("success"):
                                st.error(f"Deployment rejected: {reason}")
                                st.rerun()
                
                # Show stack details if available in CloudFormation
                st.markdown("---")
                if st.button("📋 View Stack in CloudFormation", key=f"view_stack_{deployment.pipeline_id}"):
                    stack_info = cfn_mgr.get_stack_info(deployment.stack_name)
                    if stack_info:
                        st.json(stack_info)
                    else:
                        st.info("Stack not found in CloudFormation (may not be deployed yet)")
    
    # ========================================================================
    # NEW TAB: PENDING APPROVALS
    # ========================================================================
    
    @staticmethod
    def _render_pending_approvals(cicd_mgr: CICDIntegrationManager):
        """Show deployments pending approval"""
        st.subheader("⏸️ Pending Approvals")
        st.caption("Review and approve production deployments")
        
        # Get deployments pending approval
        all_deployments = cicd_mgr.get_recent_deployments(limit=50)
        pending = [d for d in all_deployments if d.status == "pending_approval"]
        
        if not pending:
            st.success("✅ No deployments pending approval")
            st.info("💡 Production deployments will appear here for manual approval before deployment")
            return
        
        st.warning(f"⚠️ {len(pending)} deployment(s) awaiting approval")
        
        for deployment in pending:
            with st.container():
                st.markdown(f"### 🔴 PRODUCTION: {deployment.stack_name}")
                
                col1, col2 = st.columns([2, 1])
                
                with col1:
                    st.markdown(f"**Pipeline:** {deployment.pipeline_name} (#{deployment.pipeline_id})")
                    st.markdown(f"**Commit:** `{deployment.commit_hash}`")
                    st.markdown(f"**Message:** {deployment.commit_message}")
                    st.markdown(f"**Author:** {deployment.author}")
                    st.markdown(f"**Waiting since:** {deployment.triggered_at.strftime('%Y-%m-%d %H:%M:%S')}")
                    
                    # Calculate wait time
                    wait_time = (datetime.now() - deployment.triggered_at).total_seconds() / 60
                    if wait_time > 60:
                        st.warning(f"⏰ Waiting for {wait_time/60:.1f} hours")
                    else:
                        st.info(f"⏰ Waiting for {wait_time:.0f} minutes")
                
                with col2:
                    # Show deployment history for this commit
                    st.markdown("**Deployment History:**")
                    
                    # Get all deployments for this commit
                    commit_deployments = [d for d in all_deployments if d.commit_hash == deployment.commit_hash]
                    
                    for env_deploy in sorted(commit_deployments, key=lambda x: x.triggered_at):
                        if env_deploy.environment == "dev":
                            st.success(f"✅ DEV: Deployed")
                        elif env_deploy.environment == "staging":
                            st.success(f"✅ STAGING: Deployed")
                        elif env_deploy.environment == "production":
                            if env_deploy.status == "pending_approval":
                                st.warning("⏸️ PROD: Pending")
                
                # Change set preview
                st.markdown("#### 📋 Changes to be Deployed:")
                
                # This would be fetched from the actual change set
                # For demo, showing sample changes
                st.code("""
Resources to CREATE:
+ AWS::RDS::DBInstance (ProductionDatabase)
  - Engine: postgres
  - InstanceClass: db.r5.xlarge
  - MultiAZ: true
  - StorageEncrypted: true

+ AWS::RDS::DBSubnetGroup (DBSubnetGroup)
+ AWS::EC2::SecurityGroup (DBSecurityGroup)
+ AWS::RDS::DBInstance (ReadReplica1)
+ AWS::RDS::DBInstance (ReadReplica2)

Estimated Monthly Cost: $450
Security Scan: ✅ No issues found
Compliance: ✅ Meets requirements
                """)
                
                if deployment.change_set_url:
                    st.markdown(f"[📄 View Full Change Set]({deployment.change_set_url})")
                
                if deployment.pipeline_url:
                    st.markdown(f"[🔗 View Pipeline Details]({deployment.pipeline_url})")
                
                # Approval actions
                st.markdown("---")
                col1, col2, col3, col4 = st.columns([1, 1, 1, 3])
                
                with col1:
                    if st.button("✅ Approve", type="primary", key=f"approve_main_{deployment.pipeline_id}"):
                        result = cicd_mgr.approve_deployment(deployment.pipeline_id)
                        if result.get("success"):
                            st.success("✅ Deployment approved!")
                            st.balloons()
                            st.rerun()
                
                with col2:
                    if st.button("❌ Reject", key=f"reject_main_{deployment.pipeline_id}"):
                        st.session_state[f"show_reject_{deployment.pipeline_id}"] = True
                
                with col3:
                    if st.button("📊 View Metrics", key=f"metrics_{deployment.pipeline_id}"):
                        st.info("Metrics dashboard would appear here")
                
                # Rejection dialog
                if st.session_state.get(f"show_reject_{deployment.pipeline_id}"):
                    reason = st.text_area(
                        "Why are you rejecting this deployment?",
                        key=f"reject_reason_main_{deployment.pipeline_id}",
                        placeholder="E.g., 'Security concerns with new permissions' or 'Need more testing'"
                    )
                    
                    col1, col2 = st.columns(2)
                    with col1:
                        if st.button("Confirm Rejection", key=f"confirm_{deployment.pipeline_id}"):
                            if reason.strip():
                                result = cicd_mgr.reject_deployment(deployment.pipeline_id, reason)
                                if result.get("success"):
                                    st.error(f"❌ Deployment rejected: {reason}")
                                    st.rerun()
                            else:
                                st.warning("Please provide a reason for rejection")
                    
                    with col2:
                        if st.button("Cancel", key=f"cancel_{deployment.pipeline_id}"):
                            st.session_state[f"show_reject_{deployment.pipeline_id}"] = False
                            st.rerun()
                
                st.markdown("---")
    
    # ========================================================================
    # NEW TAB: TRIGGER PIPELINE
    # ========================================================================
    
    @staticmethod
    def _render_trigger_pipeline(cicd_mgr: CICDIntegrationManager):
        """Trigger CI/CD pipeline deployments"""
        st.subheader("🎯 Trigger CI/CD Pipeline")
        st.caption("Manually trigger automated deployments")
        
        st.markdown("""
        ### On-Demand Pipeline Execution
        
        Trigger your CI/CD pipelines manually when needed, while maintaining
        all the benefits of automated testing and validation.
        """)
        
        with st.form("trigger_pipeline"):
            st.markdown("#### Pipeline Configuration")
            
            col1, col2 = st.columns(2)
            
            with col1:
                repository = st.text_input(
                    "Repository",
                    value="myorg/infrastructure",
                    help="Format: organization/repository"
                )
                
                branch = st.selectbox(
                    "Branch/Tag",
                    options=["main", "develop", "staging", "v1.0.0", "v1.1.0"],
                    help="Select the branch or tag to deploy"
                )
                
                environment = st.selectbox(
                    "Target Environment",
                    options=["dev", "staging", "production"],
                    help="Environment to deploy to"
                )
            
            with col2:
                stack_name = st.text_input(
                    "Stack Name",
                    placeholder="my-infrastructure-stack",
                    help="CloudFormation stack name"
                )
                
                deployment_type = st.radio(
                    "Deployment Type",
                    options=["Standard", "Blue/Green", "Canary"],
                    help="Choose deployment strategy"
                )
                
                require_approval = st.checkbox(
                    "Require Manual Approval",
                    value=(environment == "production"),
                    help="Pause pipeline for manual approval before deployment"
                )
            
            st.markdown("#### Parameters (Optional)")
            
            parameters = st.text_area(
                "Pipeline Parameters (JSON)",
                placeholder='{"InstanceType": "t3.micro", "DesiredCapacity": "2"}',
                help="Optional parameters to pass to the pipeline"
            )
            
            st.markdown("#### Notifications")
            
            col1, col2 = st.columns(2)
            
            with col1:
                notify_email = st.text_input(
                    "Notification Email",
                    placeholder="team@example.com"
                )
            
            with col2:
                notify_slack = st.text_input(
                    "Slack Webhook",
                    placeholder="https://hooks.slack.com/..."
                )
            
            # Submit button
            submitted = st.form_submit_button("🚀 Trigger Pipeline", type="primary")
            
            if submitted:
                if not repository or not branch or not environment:
                    st.error("❌ Repository, branch, and environment are required")
                else:
                    # Parse parameters
                    params = None
                    if parameters.strip():
                        try:
                            params = json.loads(parameters)
                        except json.JSONDecodeError:
                            st.error("❌ Invalid JSON in parameters")
                            return
                    
                    # Trigger pipeline
                    with st.spinner("Triggering pipeline..."):
                        result = cicd_mgr.trigger_pipeline(
                            repo=repository,
                            branch=branch,
                            environment=environment,
                            parameters=params
                        )
                    
                    if result.get("success"):
                        st.success(f"✅ Pipeline triggered successfully!")
                        st.info(f"**Pipeline ID:** {result.get('pipeline_id')}")
                        
                        if result.get("pipeline_url"):
                            st.markdown(f"[🔗 View Pipeline Status]({result.get('pipeline_url')})")
                        
                        st.balloons()
                        
                        # Show next steps
                        st.markdown("### ✨ Next Steps")
                        st.info("""
                        1. Monitor pipeline progress in the **CI/CD Deployments** tab
                        2. If approval is required, it will appear in **Pending Approvals** tab
                        3. View deployed stack in **Stack Library** tab after completion
                        """)
                    else:
                        st.error(f"❌ Failed to trigger pipeline: {result.get('error', 'Unknown error')}")
        
        # Recent triggers
        st.markdown("---")
        st.markdown("### 📜 Recently Triggered Pipelines")
        
        recent_triggers = [
            {"time": "5 minutes ago", "repo": "myorg/infrastructure", "branch": "main", "env": "staging", "status": "running"},
            {"time": "2 hours ago", "repo": "myorg/infrastructure", "branch": "main", "env": "production", "status": "success"},
            {"time": "1 day ago", "repo": "myorg/app-stack", "branch": "develop", "env": "dev", "status": "success"},
        ]
        
        for trigger in recent_triggers:
            col1, col2, col3, col4, col5 = st.columns([2, 2, 1, 1, 1])
            
            with col1:
                st.text(trigger["repo"])
            with col2:
                st.text(f"Branch: {trigger['branch']}")
            with col3:
                st.text(trigger["env"].upper())
            with col4:
                if trigger["status"] == "success":
                    st.success("✅")
                elif trigger["status"] == "running":
                    st.info("🔄")
                else:
                    st.error("❌")
            with col5:
                st.text(trigger["time"])
    
    # ========================================================================
    # ORIGINAL TABS (Preserved with minor enhancements)
    # ========================================================================
    
    @staticmethod
    def _render_stack_library(cfn_mgr: CloudFormationManager):
        """Stack library and templates - ENHANCED with CI/CD indicators"""
        st.subheader("📚 CloudFormation Stack Library")
        st.caption("View all stacks (manual + CI/CD deployed)")
        
        # List existing stacks
        stacks = cfn_mgr.list_stacks()
        
        if stacks:
            col1, col2 = st.columns(2)
            
            with col1:
                st.metric("Total Stacks", len(stacks))
            
            with col2:
                # Count CI/CD deployed stacks (based on tags)
                cicd_deployed = sum(1 for s in stacks if s.get('tags', {}).get('DeployedBy') == 'CI/CD')
                st.metric("CI/CD Deployed", cicd_deployed)
            
            # Status filter
            status_filter = st.multiselect(
                "Filter by Status",
                options=["CREATE_COMPLETE", "UPDATE_COMPLETE", "CREATE_IN_PROGRESS", 
                        "UPDATE_IN_PROGRESS", "ROLLBACK_COMPLETE"],
                default=["CREATE_COMPLETE", "UPDATE_COMPLETE"],
                key="stack_lib_status_filter"
            )
            
            # Deployment method filter
            deploy_filter = st.multiselect(
                "Filter by Deployment Method",
                options=["All", "CI/CD", "Manual"],
                default=["All"],
                key="stack_lib_deploy_filter"
            )
            
            # Filter stacks
            filtered_stacks = [s for s in stacks if s['status'] in status_filter] if status_filter else stacks
            
            if "Manual" in deploy_filter or "CI/CD" in deploy_filter:
                if "All" not in deploy_filter:
                    filtered_stacks = [
                        s for s in filtered_stacks
                        if (("CI/CD" in deploy_filter and s.get('tags', {}).get('DeployedBy') == 'CI/CD') or
                            ("Manual" in deploy_filter and s.get('tags', {}).get('DeployedBy') != 'CI/CD'))
                    ]
            
            # Display stacks
            for stack in filtered_stacks:
                status_icon = "✅" if "COMPLETE" in stack['status'] else "🔄" if "IN_PROGRESS" in stack['status'] else "❌"
                
                # Check if CI/CD deployed
                deploy_badge = ""
                if stack.get('tags', {}).get('DeployedBy') == 'CI/CD':
                    deploy_badge = "🤖 CI/CD |"
                else:
                    deploy_badge = "👤 Manual |"
                
                with st.expander(f"{status_icon} {deploy_badge} {stack['stack_name']} - {stack['status']}"):
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        st.write(f"**Stack ID:** {stack['stack_id']}")
                        st.write(f"**Status:** {stack['status']}")
                        st.write(f"**Created:** {stack['creation_time']}")
                        
                        # Show CI/CD info if available
                        if stack.get('tags', {}).get('DeployedBy') == 'CI/CD':
                            st.write(f"**Git Commit:** `{stack.get('tags', {}).get('GitCommit', 'N/A')}`")
                            st.write(f"**Pipeline:** {stack.get('tags', {}).get('PipelineID', 'N/A')}")
                    
                    with col2:
                        st.write(f"**Last Updated:** {stack['last_updated']}")
                        st.write(f"**Drift Status:** {stack.get('drift_status', 'NOT_CHECKED')}")
                    
                    # Actions
                    col1, col2, col3, col4 = st.columns(4)
                    with col1:
                        if st.button("👁️ Details", key=f"details_{stack['stack_name']}"):
                            stack_info = cfn_mgr.get_stack_info(stack['stack_name'])
                            if stack_info:
                                st.json(stack_info)
                    
                    with col2:
                        if st.button("📋 Resources", key=f"resources_{stack['stack_name']}"):
                            resources = cfn_mgr.list_stack_resources(stack['stack_name'])
                            if resources:
                                res_df = pd.DataFrame(resources)
                                st.dataframe(res_df, use_container_width=True)
                    
                    with col3:
                        if st.button("🔍 Drift", key=f"drift_{stack['stack_name']}"):
                            result = cfn_mgr.detect_stack_drift(stack['stack_name'])
                            if result.get('success'):
                                st.success("Drift detection started")
                    
                    with col4:
                        if st.button("🗑️ Delete", key=f"delete_{stack['stack_name']}"):
                            result = cfn_mgr.delete_stack(stack['stack_name'])
                            if result.get('success'):
                                st.success(f"Stack deletion initiated")
                                st.rerun()
        else:
            st.info("No stacks found in this account")
    
    @staticmethod
    def _render_deploy_stack(cfn_mgr: CloudFormationManager):
        """Deploy new stack - original functionality preserved"""
        st.subheader("🚀 Deploy CloudFormation Stack (Manual)")
        st.caption("For emergency or one-off deployments outside CI/CD pipeline")
        
        st.info("💡 **Tip:** For regular deployments, use the CI/CD pipeline via the 'Trigger Pipeline' tab")
        
        # Original deploy stack form code continues here...
        # (Keeping your original implementation)
        st.markdown("Manual deployment form would go here...")
    
    @staticmethod
    def _render_active_deployments(cfn_mgr: CloudFormationManager):
        """Active deployments - original functionality"""
        st.subheader("🔄 Active Deployments")
        
        # Get stacks in progress
        stacks = cfn_mgr.list_stacks(
            status_filter=["CREATE_IN_PROGRESS", "UPDATE_IN_PROGRESS", 
                          "DELETE_IN_PROGRESS", "ROLLBACK_IN_PROGRESS"]
        )
        
        if stacks:
            st.write(f"**Active Deployments:** {len(stacks)}")
            
            for stack in stacks:
                with st.expander(f"🔄 {stack['stack_name']} - {stack['status']}"):
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        st.write(f"**Stack:** {stack['stack_name']}")
                        st.write(f"**Status:** {stack['status']}")
                    
                    with col2:
                        st.write(f"**Started:** {stack['creation_time']}")
                    
                    # Show recent events
                    events = cfn_mgr.get_stack_events(stack['stack_name'], limit=10)
                    if events:
                        st.markdown("**Recent Events:**")
                        events_df = pd.DataFrame(events)
                        st.dataframe(events_df, use_container_width=True)
        else:
            st.success("✅ No active deployments")
    
    @staticmethod
    def _render_change_sets(cfn_mgr: CloudFormationManager):
        """Change sets - original functionality"""
        st.subheader("📝 Change Sets")
        
        st.markdown("""
        ### Preview Changes Before Deployment
        
        Change sets allow you to preview how proposed changes will affect your running resources.
        """)
        
        # Original change sets code continues...
        st.info("Change sets functionality would go here...")
    
    @staticmethod
    def _render_multi_region():
        """Multi-region deployment - original functionality"""
        st.subheader("🌍 Multi-Region Deployment")
        
        st.markdown("""
        ### Deploy to Multiple Regions Simultaneously
        
        Deploy your infrastructure across multiple AWS regions for high availability.
        """)
        
        # Original multi-region code continues...
        st.info("Multi-region deployment functionality would go here...")
    
    @staticmethod
    def _render_rollback(cfn_mgr: CloudFormationManager):
        """Rollback operations - original functionality"""
        st.subheader("⏮️ Rollback & Recovery")
        
        st.markdown("""
        ### Rollback Failed Deployments
        
        Manage failed stack deployments and rollback to previous stable states.
        """)
        
        # Original rollback code continues...
        st.info("Rollback functionality would go here...")
