/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `properties`
--

-- --------------------------------------------------------

--
-- Table structure for table `rightmove`
--

CREATE TABLE `rightmove` (
  `web_key` varchar(256) NOT NULL,
  `name` text NOT NULL,
  `address` text NOT NULL,
  `url` text NOT NULL,
  `price` text NOT NULL,
  `timestamp` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `spareroom`
--

CREATE TABLE `spareroom` (
  `web_key` varchar(256) NOT NULL,
  `name` text NOT NULL,
  `address` text NOT NULL,
  `url` text NOT NULL,
  `price` text NOT NULL,
  `timestamp` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `rightmove`
--
ALTER TABLE `rightmove`
  ADD PRIMARY KEY (`web_key`);

--
-- Indexes for table `spareroom`
--
ALTER TABLE `spareroom`
  ADD PRIMARY KEY (`web_key`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
