using CafeTimeManager.Core.Models;
using CafeTimeManager.Data.Context;
using Microsoft.EntityFrameworkCore;
using System.Collections.Generic;
using System.Linq;

namespace CafeTimeManager.Data.Repositories
{
    public class SessionRepository
    {
        private readonly AppDbContext _context;

        public SessionRepository(AppDbContext context)
        {
            _context = context;
        }

        public void StartSession(User user)
        {
            var session = new UserSession
            {
                UserId = user.Id,
                Username = user.Username,
                StartTime = DateTime.Now
            };

            _context.Add(session);
            _context.SaveChanges();
        }

        public void EndSession(User user)
        {
            var activeSession = _context.Set<UserSession>()
                .Where(s => s.UserId == user.Id && s.EndTime == null)
                .OrderByDescending(s => s.StartTime)
                .FirstOrDefault();

            if (activeSession != null)
            {
                activeSession.EndTime = DateTime.Now;
                _context.SaveChanges();
            }
        }

        public List<UserSession> GetAllSessions()
        {
            return _context.Set<UserSession>()
                .OrderByDescending(s => s.StartTime)
                .ToList();
        }
    }
}
