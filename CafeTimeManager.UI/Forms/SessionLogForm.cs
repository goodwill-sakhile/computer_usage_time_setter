using CafeTimeManager.Data.Repositories;
using System;
using System.Linq;
using System.Windows.Forms;

namespace CafeTimeManager.UI.Forms
{
    public partial class SessionLogForm : Form
    {
        private readonly SessionRepository _sessionRepo;

        public SessionLogForm(SessionRepository sessionRepo)
        {
            InitializeComponent();
            _sessionRepo = sessionRepo;
            LoadLogs();
        }

        private void LoadLogs()
        {
            var sessions = _sessionRepo.GetAllSessions();

            foreach (var session in sessions)
            {
                string[] row = {
                    session.Username,
                    session.StartTime.ToString("g"),
                    session.EndTime?.ToString("g") ?? "Active",
                    session.GetDuration().ToString(@"hh\:mm\:ss")
                };

                dgvLogs.Rows.Add(row);
            }
        }
    }
}
