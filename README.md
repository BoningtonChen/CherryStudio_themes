# Maple Neon: A Theme for Cherry Studio

![Free Palestine](https://freepalestinemovement.org/wp-content/uploads/2013/06/banner.jpg)
![Cherry Studio](https://www.cherry-ai.com/assets/cherry-logo-CtmH594q.svg)
![Static Badge](https://img.shields.io/badge/Tailored_for-Cherry_Studio-red?logo=Github)
![Static Badge](https://img.shields.io/badge/License-MIT-blue)
![Static Badge](https://img.shields.io/badge/Language-CSS-pink?logo=css)
![Static Badge](https://img.shields.io/badge/Release-v1.2.1-green)
<div style="text-align: center">
English |
<a href="https://github.com/BoningtonChen/CherryStudio_themes/blob/master/docs/README.zh.md">中文</a> |
<a href="https://github.com/BoningtonChen/CherryStudio_themes/blob/master/docs/README.fr.md">Français</a> |
<a href="https://github.com/BoningtonChen/CherryStudio_themes/blob/master/docs/README.ja.md">日本語</a>
</div>

## Introduction

This is a theme tailored for Cherry Studio, a desktop client that supports for multiple LLM providers, available on Windows, Mac and Linux. \
For more information about Cherry Studio, check [here](https://github.com/CherryHQ/cherry-studio).

## How to USE

1. (Recommended but not necessary) Download Maple Mono NF CN from [Maple Font](https://github.com/subframe7536/maple-font/releases/download/v7.3/MapleMono-NF-CN-unhinted.zip). If you do not like the font, the default fallback font should be `Fira Code`.
2. (Recommended but not necessary) Download DreamHan Sans and DreamHan Serif from [DreamHan Font](https://github.com/Pal3love/dream-han-cjk/releases). If you do not like the font, the system will use Microsoft YaHei as fallback font.
3. Copy the content in [maple-neon.css](./themes/maple-neon.css) file(for original version) or download the raw file(for customization).
4. Paste it into Cherry Studio.
5. Here you go!

<details>
<summary>Or, if you don't want to modify, directly copy CSS from here!</summary>

```css
/* Maple Neon Theme Font Minimal: A Maple Neon theme version that only specifies the font */

/* 动画定义 */
@keyframes clickAnimation {
    0% {
        opacity: 1;
    }
    50% {
        opacity: 0.7; /* 轻微的透明度变化作为点击反馈，增强动画效果 */
    }
    100% {
        opacity: 1;
    }
}

@keyframes page-popup-right {
    from {
        transform: translateX(-2em);
        opacity: 0;
    }
    to {
        transform: translateX(0);
        opacity: 100%;
    }
}

@keyframes page-popup-left {
    from {
        transform: translateX(2em);
        opacity: 0;
    }
    to {
        transform: translateX(0);
        opacity: 100%;
    }
}

/* 基础变量定义 */
:root {
    //   --chat-background-assistant: #fff;
    //   --color-border: rgba(120, 120, 120, 0.08) !important;

    /* --- 动画相关变量 --- */
    --animation: cubic-bezier(0.25, 0.1, 0.25, 1); /* 调整为更快的 ease-out */
    --short-timer: 0.15s; /* 缩短时间 */
    --long-timer: 0.3s; /* 缩短时间 */
    --button-border-radius: 12px;
    --button-border-radius-hover: 12px; /* 保持 hover 时圆角不变 */
    --button-border-radius-active: 12px; /* 保持 active 时圆角不变 */

    /* --- 字体规范对齐 --- */
    /* 基础字体 (对应规范中的 --font-family) */
    --content-font: "Microsoft YaHei", "微软雅黑", "DreamHan Serif", "梦源宋体", "Noto Sans", "Noto Sans SC", Ubuntu, -apple-system,
    BlinkMacSystemFont, "Segoe UI", system-ui, Roboto, Oxygen, Cantarell, "Open Sans", "Helvetica Neue", Arial,
    "Noto Sans", sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji" !important;
    --content-font-weight: normal;

    /* 标题/UI 字体 (对应规范中的 --font-family-serif, 但这里保持无衬线优先) */
    --title-font: "Microsoft YaHei", "微软雅黑", "DreamHan Sans", "梦源黑体", "Noto Serif", "Noto Serif SC", "Microsoft Sans", -apple-system,
    BlinkMacSystemFont, "Segoe UI", system-ui, Ubuntu, Roboto, Oxygen, Cantarell, "Open Sans", "Helvetica Neue",
    serif, Arial, "Noto Sans", "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji" !important;
    --title-font-weight: bold;

    /* 代码字体 (对应规范中的 --code-font-family) */
    --monospace-font: "Maple Mono", "Maple Mono NF CN", "Cascadia Code", "Fira Code", "Consolas", Menlo, Courier, monospace !important;
    --monospace-font-weight: normal;

    --ui-font-weight: bold; /* 保留UI元素的特定粗细控制 */

    // --input-gradient-opacity: 1;

    //   --box-shadow-message: 0 4px 16px -8px rgba(0, 0, 0, 0.04);
    //   --border-radius-message: 16px;
}

/* 消息容器样式：增加霓虹AI助手效果 */
/* 输入框动画效果 */
@keyframes gradientFlow {
    0% {
        background-position: 0 50%;
    }

    50% {
        background-position: 100% 50%;
    }

    100% {
        background-position: 0 50%;
    }
}

#inputbar::before {
    content: "";
    position: absolute;
    inset: -2px;
    border-radius: inherit;
    padding: 3px;
    background: linear-gradient(
                    90deg,
                    #ff6a01,
                /* 爱马仕橙，原色：#d65f00 */ #f8c91c,
                /* 那不勒斯黄，原色：#ffb800 */ #8a2be2,
                /* 紫罗兰色，原色：#8a2be2 */ #f8c91c,
                /* #ffb800 */ #ff6901 /* #d65e00 */
    );
    background-size: 200% 200%;
    mask:
            linear-gradient(#000 0 0) content-box,
            linear-gradient(#000 0 0);
    -webkit-mask-composite: destination-out; /* 兼容旧版 WebKit 内核浏览器 */
    mask-composite: exclude;
    animation: gradientFlow 4s linear infinite;
    opacity: 0;
    transition: all 0.4s ease-in-out;
    pointer-events: auto;
}

#inputbar:focus-within::before {
    opacity: 1;
}

/* 字体样式更改 */
/* UI元素使用粗体 */
body,
div:not(.message-content-container),
span:not(.message-content-container span),
h1,
h2,
h3,
h4,
h5,
h6,
header,
nav,
.sidebar,
.menu,
.button,
.tabs,
.navigation,
.header,
.footer,
.title {
    font-family: var(--title-font), sans-serif;
    font-weight: var(--title-font-weight);
}

/* 消息内容和输入区域 */
.message-content-container,
.message-content-container *,
p,
li,
ul,
ol,
.form-control,
#inputbox,
textarea {
    font-family: var(--content-font), sans-serif;
    font-weight: var(--content-font-weight);
}

/* 代码块和内联代码的特殊字体处理 */
pre,
pre *,
code,
.markdown-body pre,
.markdown-body pre *,
.markdown-body code {
    font-family: var(--monospace-font), monospace !important;
    font-weight: var(--monospace-font-weight);
    -webkit-font-feature-settings:
            "liga" 1,
            "calt" 1,
            "ss01" 1,
            "ss02" 1,
            "ss03" 1,
            "zero" 1 !important;
    font-feature-settings:
            "liga" 1,
            "calt" 1,
            "ss01" 1,
            "ss02" 1,
            "ss03" 1,
            "zero" 1 !important;
    text-rendering: optimizeLegibility;
}
```

</details>

## What's special about the theme?

- It provides modernized and aesthetic UI for Cherry Studio.
- It mixes the Maple font with a neon-styled input-bar, creating a unique and visually appealing experience.
- Uses DreamHan font series and Microsoft YaHei to provide excellent Chinese font display effects.

## Demonstration

Based on Cherry Studio v1.2.4
![Page Light](./examples/main-page-light.png)

![Page Dark](./examples/main-page-dark.png)

## Customization

You can fork the project and modify your own theme for Cherry Studio, for exact instructions, check [Cherry Studio Docs](https://docs.cherry-ai.com/personalization-settings/css).

## One more Glance

For other themes, check [One More Glance](./OneMoreGlance.md)

## Inspiration

### Themes

- Dracula Theme: <https://cherrycss.com>
- Neon Theme: <https://cherry-ai.com/css>

### Fonts

- Maple Font: <https://github.com/subframe7536/maple-font>
- DreamHan Sans: <https://github.com/Pal3love/dream-han-cjk/releases>

### Tools

- The Themes are constructed partly under the help of DeepSeek-0324 & Claude-3.7.

## LICENSE

The Project follows [MIT LICENSE](./LICENSE).
