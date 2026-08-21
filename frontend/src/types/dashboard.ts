export interface PriceChange {
  name: string
  current: number
  old: number
  change_percent: number
  change_amount: number
}

export interface LastPriceUpdateBy {
  username: string | null
  full_name: string | null
  at: string
}

export interface RecentPriceUpdate {
  price_type: string
  category: string | null
  price: number
  updated_at: string
}

export interface DashboardSummary {
  degraded?: boolean
  highest_price: number
  highest_price_label: string
  avg_24h_change: number
  biggest_change: PriceChange | null
  price_changes: PriceChange[]
  total_bots: number
  active_bots: number
  total_channels: number
  active_channels: number
  total_price_types: number
  total_price_updates: number
  latest_update_time: string | null
  recent_updates_24h: number
  last_price_update_by: LastPriceUpdateBy | null
  recent_price_updates: RecentPriceUpdate[]
}

export interface DailyUsage {
  date: string
  active_users: number
}

export interface ChannelSnapshot {
  channel_id: number
  name: string
  member_count: number
  sampled_at: string | null
}

export interface BotInfo {
  id: number
  name: string
  display_name: string
  is_active: boolean
  channel_count: number
}

export interface TelegramStats {
  daily_usage: DailyUsage[]
  channel_snapshots: ChannelSnapshot[]
  total_active_users_yesterday: number
  total_members: number
  bots: BotInfo[]
}

export interface ExchangeRequestCustomer {
  id: number
  telegram_user_id: number
  username: string | null
  first_name: string | null
  last_name: string | null
}

export interface ExchangeRequest {
  id: number
  customer: ExchangeRequestCustomer
  source_currency: string
  target_currency: string
  amount: string
  ttl_minutes: number
  status: 'new' | 'cancelled' | 'successful'
  created_at: string
  updated_at: string
}
