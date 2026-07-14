"""UI Theme"""
package com.nexusai.app.ui.theme

import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.darkColorScheme
import androidx.compose.material3.lightColorScheme
import androidx.compose.runtime.Composable
import androidx.compose.ui.graphics.Color

private val DarkColorScheme = darkColorScheme(
    primary = Color(0xFF00D9FF),
    secondary = Color(0xFF7B00FF),
    tertiary = Color(0xFF00FF88),
    background = Color(0xFF0A0E27),
    surface = Color(0xFF1A1F3A),
    error = Color(0xFFFF5555)
)

private val LightColorScheme = lightColorScheme(
    primary = Color(0xFF0066CC),
    secondary = Color(0xFF7B00FF),
    tertiary = Color(0xFF00AA44),
    background = Color(0xFFFAFBFC),
    surface = Color(0xFFFFFFFF),
    error = Color(0xFFCC0000)
)

@Composable
fun NexusAITheme(
    darkTheme: Boolean = true,
    content: @Composable () -> Unit
) {
    val colorScheme = if (darkTheme) DarkColorScheme else LightColorScheme
    
    MaterialTheme(
        colorScheme = colorScheme,
        typography = androidx.compose.material3.Typography(),
        content = content
    )
}
