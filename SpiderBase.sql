/*
 Navicat Premium Data Transfer

 Source Server         : localhost 2
 Source Server Type    : MySQL
 Source Server Version : 50713
 Source Host           : localhost
 Source Database       : SpiderBase

 Target Server Type    : MySQL
 Target Server Version : 50713
 File Encoding         : utf-8

 Date: 03/23/2018 14:13:58 PM
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
--  Table structure for `MM176Type`
-- ----------------------------
DROP TABLE IF EXISTS `MM176Type`;
CREATE TABLE `MM176Type` (
  `name` varchar(100) NOT NULL,
  `url` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
--  Table structure for `MMItem`
-- ----------------------------
DROP TABLE IF EXISTS `MMItem`;
CREATE TABLE `MMItem` (
  `title` varchar(255) DEFAULT NULL,
  `href` varchar(255) DEFAULT NULL,
  `tags` varchar(255) DEFAULT NULL,
  `id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
--  Table structure for `ProxyInfo`
-- ----------------------------
DROP TABLE IF EXISTS `ProxyInfo`;
CREATE TABLE `ProxyInfo` (
  `ip` varchar(100) NOT NULL,
  `port` varchar(100) DEFAULT NULL,
  `Type` varchar(100) DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4999 DEFAULT CHARSET=utf8;

SET FOREIGN_KEY_CHECKS = 1;
