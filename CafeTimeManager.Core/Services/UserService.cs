using CafeTimeManager.Core.Interfaces;
using CafeTimeManager.Core.Models;
using System.Collections.Generic;
using System.Linq;

namespace CafeTimeManager.Core.Services
{
    public class UserService : IUserService
    {
        private readonly List<User> _users = new List<User>();
        private int _nextId = 1;

        public void AddUser(User user)
        {
            user.Id = _nextId++;
            _users.Add(user);
        }

        public void RemoveUser(int userId)
        {
            var user = _users.FirstOrDefault(u => u.Id == userId);
            if (user != null)
                _users.Remove(user);
        }

        public void StartUserSession(int userId)
        {
            var user = GetUser(userId);
            if (user != null && !user.IsSessionExpired())
            {
                user.StartSession();
            }
        }

        public void EndUserSession(int userId)
        {
            var user = GetUser(userId);
            if (user != null && user.IsActive)
            {
                user.EndSession();
            }
        }

        public User GetUser(int userId)
        {
            return _users.FirstOrDefault(u => u.Id == userId);
        }

        public List<User> GetAllUsers()
        {
            return _users;
        }
    }
}
