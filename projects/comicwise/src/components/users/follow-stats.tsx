/**
 * Follow Stats Component
 * Display follower and following counts
 */

interface FollowStatsProps {
  followers: number;
  following: number;
}

export function FollowStats({ followers, following }: FollowStatsProps) {
  return (
    <div className="flex gap-4">
      <div className="text-center">
        <div className="font-semibold">{followers}</div>
        <div className="text-sm text-muted-foreground">Followers</div>
      </div>
      <div className="text-center">
        <div className="font-semibold">{following}</div>
        <div className="text-sm text-muted-foreground">Following</div>
      </div>
    </div>
  );
}
