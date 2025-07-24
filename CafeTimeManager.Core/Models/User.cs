namespace CafeTimeManager.Core.Models
{
    public class User
    {
        public int Id { get; set; }
        public string Username { get; set; }
        public TimeSpan TimeAllocated { get; set; }
        public TimeSpan TimeRemaining { get; set; }
        public DateTime SessionStart { get; set; }
        public bool IsActive { get; set; }

        public void StartSession()
        {
            SessionStart = DateTime.Now;
            IsActive = true;
        }

        public void EndSession()
        {
            IsActive = false;
            TimeRemaining = TimeRemaining - (DateTime.Now - SessionStart);
        }

        public bool IsSessionExpired()
        {
            return TimeRemaining <= TimeSpan.Zero;
        }
    }
}
