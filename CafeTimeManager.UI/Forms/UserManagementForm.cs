using System;
using System.Windows.Forms;
using CafeTimeManager.Core.Interfaces;
using CafeTimeManager.Core.Models;

namespace CafeTimeManager.UI.Forms
{
    public partial class UserManagementForm : Form
    {
        private readonly IUserService _userService;

        public UserManagementForm(IUserService userService)
        {
            InitializeComponent();
            _userService = userService;
            RefreshUserList();
        }

        private void RefreshUserList()
        {
            lstUsers.Items.Clear();
            foreach (var user in _userService.GetAllUsers())
            {
                lstUsers.Items.Add($"{user.Id} - {user.Username} - {user.TimeRemaining.TotalMinutes} min");
            }
        }

        private void btnAddUser_Click(object sender, EventArgs e)
        {
            var username = txtUsername.Text;
            var minutes = (int)numMinutes.Value;

            var user = new User
            {
                Username = username,
                TimeAllocated = TimeSpan.FromMinutes(minutes),
                TimeRemaining = TimeSpan.FromMinutes(minutes),
                IsActive = false
            };

            _userService.AddUser(user);
            RefreshUserList();
        }

        private void btnStartSession_Click(object sender, EventArgs e)
        {
            if (int.TryParse(txtUserId.Text, out int userId))
            {
                _userService.StartUserSession(userId);
                RefreshUserList();
            }
        }

        private void btnEndSession_Click(object sender, EventArgs e)
        {
            if (int.TryParse(txtUserId.Text, out int userId))
            {
                _userService.EndUserSession(userId);
                RefreshUserList();
            }
        }
    }
}
