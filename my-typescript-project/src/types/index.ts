export interface AppConfig {
    port: number;
    dbUrl: string;
    environment: 'development' | 'production';
}