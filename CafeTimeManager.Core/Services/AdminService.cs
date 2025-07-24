using CafeTimeManager.Core.Interfaces;
using CafeTimeManager.Core.Models;

namespace CafeTimeManager.Core.Services
{
    public class AdminService : IAdminService
    {
        private Admin _admin;

        public void SetAdmin(Admin admin)
        {
            _admin = admin;
        }

        public bool Login(string username, string password)
        {
            if (_admin == null) return false;
            return _admin.Username == username && _admin.Authenticate(password);
        }
    }
}
