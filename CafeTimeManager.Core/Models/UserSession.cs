using System;

namespace CafeTimeManager.Core.Models
{
    public class UserSession
    {
        public int Id { get; set; }
        public int UserId { get; set; }
        public string Username { get; set; }
        public DateTime StartTime { get; set; }
        public DateTime? EndTime { get; set; }

        public TimeSpan GetDuration()
        {
            return (EndTime ?? DateTime.Now) - StartTime;
        }
    }
}
