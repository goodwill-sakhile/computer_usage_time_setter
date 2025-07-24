using CafeTimeManager.Core.Models;
using System.Collections.Generic;

namespace CafeTimeManager.Core.Interfaces
{
    public interface IUserService
    {
        void AddUser(User user);
        void RemoveUser(int userId);
        void StartUserSession(int userId);
        void EndUserSession(int userId);
        User GetUser(int userId);
        List<User> GetAllUsers();
    }
}
