namespace CafeTimeManager.Common.Extensions
{
    public static class StringExtensions
    {
        public static bool IsEmpty(this string input)
        {
            return string.IsNullOrWhiteSpace(input);
        }

        public static string TrimSafe(this string input)
        {
            return input?.Trim() ?? string.Empty;
        }
    }
}
