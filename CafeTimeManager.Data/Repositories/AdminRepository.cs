using CafeTimeManager.Core.Models;
using Microsoft.EntityFrameworkCore;
using System.Linq;

namespace CafeTimeManager.Data.Repositories
{
    public class AdminRepository
    {
        private readonly Context.AppDbContext _context;

        public AdminRepository(Context.AppDbContext context)
        {
            _context = context;
        }

        public Admin GetAdminByUsername(string username)
        {
            return _context.Admins.FirstOrDefault(a => a.Username == username);
        }

        public void SetAdmin(Admin admin)
        {
            var existing = _context.Admins.FirstOrDefault();
            if (existing == null)
                _context.Admins.Add(admin);
            else
            {
                existing.Username = admin.Username;
                existing.PasswordHash = admin.PasswordHash;
                _context.Admins.Update(existing);
            }
            _context.SaveChanges();
        }
    }
}
