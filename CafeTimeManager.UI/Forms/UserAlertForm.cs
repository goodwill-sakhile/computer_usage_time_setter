using System;
using System.Windows.Forms;

namespace CafeTimeManager.UI.Forms
{
    public partial class UserAlertForm : Form
    {
        public UserAlertForm(string username, string message)
        {
            InitializeComponent();
            lblUser.Text = username;
            lblMessage.Text = message;
        }

        private void btnOk_Click(object sender, EventArgs e)
        {
            this.Close();
        }
    }
}
