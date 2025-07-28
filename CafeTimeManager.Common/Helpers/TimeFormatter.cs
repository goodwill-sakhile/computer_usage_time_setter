namespace CafeTimeManager.Common.Helpers
{
    public static class TimeFormatter
    {
        public static string ToReadableFormat(this TimeSpan time)
        {
            return time.ToString(@"hh\:mm\:ss");
        }

        public static string RemainingOrExpired(this TimeSpan time)
        {
            return time.TotalSeconds <= 0 ? "Expired" : ToReadableFormat(time);
        }
    }
}
