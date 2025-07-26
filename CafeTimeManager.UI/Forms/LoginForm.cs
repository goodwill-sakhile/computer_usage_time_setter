using System;
using System.Windows.Forms;
using CafeTimeManager.Core.Interfaces;

namespace CafeTimeManager.UI.Forms
{
    public partial class LoginForm : Form
    {
        private readonly IAdminService _adminService;

        public LoginForm(IAdminService adminService)
        {
            InitializeComponent();
            _adminService = adminService;
        }

        private void btnLogin_Click(object sender, EventArgs e)
        {
            string username = txtUsername.Text;
            string password = txtPassword.Text;

            if (_adminService.Login(username, password))
            {
                this.Hide();
                var dashboard = new DashboardForm();
                dashboard.Show();
            }
            else
            {
                MessageBox.Show("Invalid credentials.", "Login Failed", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }
    }
}
